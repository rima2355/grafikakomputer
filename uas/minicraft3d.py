from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

# Variabel untuk menyimpan blok
blocks = []

# Kelas untuk setiap blok
class Voxel(Button):
    def __init__(self, position=(0,0,0), texture='white_cube', block_color=color.white):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=texture,
            color=block_color,
            highlight_color=color.lime,
        )
        blocks.append(self)
    
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                # Hancurkan blok
                if self in blocks:
                    blocks.remove(self)
                destroy(self)
            
            if key == 'right mouse down':
                # Buat blok baru di sisi yang diklik
                new_pos = self.position + mouse.normal
                col = app.current_color
                new_block = Voxel(position=new_pos, texture='white_cube', block_color=col)
                print(f"✓ Blok baru dibuat di posisi: {new_pos}")

# Buat ground (tanah) dengan grass
print("Membuat tanah...")
for z in range(-15, 16):
    for x in range(-15, 16):
        Voxel(position=(x, 0, z), block_color=color.rgb(34, 139, 34))

# Buat pohon sederhana
print("Menanam pohon...")

def create_tree(x, z):
    # Batang (coklat)
    for y in range(1, 5):
        Voxel(position=(x, y, z), block_color=color.rgb(139, 69, 19))
    
    # Daun (hijau) - bentuk kubus
    for dy in range(5, 8):
        for dx in range(-1, 2):
            for dz in range(-1, 2):
                if not (dx == 0 and dz == 0 and dy == 7):  # Skip puncak tengah
                    Voxel(position=(x+dx, dy, z+dz), block_color=color.rgb(0, 200, 0))

# Tanam 5 pohon di posisi yang berbeda
tree_positions = [(-8, 8), (-5, -6), (5, 7), (8, -8), (-10, 0)]
for tx, tz in tree_positions:
    create_tree(tx, tz)

# Buat rumah sederhana
print("Membangun rumah...")

def create_house(x, z):
    # Lantai (abu-abu)
    for dx in range(6):
        for dz in range(6):
            Voxel(position=(x+dx, 1, z+dz), block_color=color.gray)
    
    # Dinding (coklat muda)
    wall_color = color.rgb(210, 180, 140)
    
    # Dinding depan dan belakang
    for dx in range(6):
        for dy in range(2, 5):
            Voxel(position=(x+dx, dy, z), block_color=wall_color)
            Voxel(position=(x+dx, dy, z+5), block_color=wall_color)
    
    # Dinding kiri dan kanan
    for dz in range(1, 5):
        for dy in range(2, 5):
            Voxel(position=(x, dy, z+dz), block_color=wall_color)
            Voxel(position=(x+5, dy, z+dz), block_color=wall_color)
    
    # Atap (merah)
    roof_color = color.rgb(180, 0, 0)
    for dx in range(-1, 7):
        for dz in range(-1, 7):
            Voxel(position=(x+dx, 5, z+dz), block_color=roof_color)
    
    # Atap tingkat 2
    for dx in range(0, 6):
        for dz in range(0, 6):
            Voxel(position=(x+dx, 6, z+dz), block_color=roof_color)
    
    # Pintu - buat space untuk pintu
    # (Kita buat pintunya dengan warna berbeda)
    Voxel(position=(x+2, 2, z), block_color=color.rgb(101, 67, 33))
    Voxel(position=(x+2, 3, z), block_color=color.rgb(101, 67, 33))

# Bangun rumah di koordinat tertentu
create_house(0, -10)

# Player
player = FirstPersonController()
player.position = (0, 10, 15)  # Start di atas agar bisa lihat keseluruhan
player.speed = 5
player.gravity = 0.5

# Sky
sky = Sky()
sky.color = color.rgb(135, 206, 235)

# Variabel untuk block selector
app.current_texture = 'white_cube'
app.current_color = color.rgb(34, 139, 34)  # Default grass

# UI
info_text = Text(
    text='',
    position=(-0.85, 0.45),
    scale=1.2,
    origin=(0, 0),
    background=True
)

block_type_text = Text(
    text='Block: Grass [1]',
    position=(0.5, -0.45),
    scale=1.5,
    origin=(0, 0),
    background=True
)

# Instruksi Build
build_instruction = Text(
    text='[KLIK KANAN pada balok untuk menambah balok baru]',
    position=(0, 0.48),
    scale=1.3,
    origin=(0, 0),
    background=True,
    color=color.yellow
)

# Crosshair
crosshair = Entity(
    parent=camera.ui,
    model='quad',
    color=color.white,
    scale=0.008,
    rotation_z=45
)

def update():
    info_text.text = f'Minecraft Game | Posisi: ({int(player.x)}, {int(player.y)}, {int(player.z)}) | Total Blok: {len(blocks)}\nWASD: Gerak | SPACE: Lompat | Mouse: Lihat\nKLIK KIRI: Hancurkan | KLIK KANAN: Tambah Balok\n1-5: Pilih Blok | ESC: Keluar'

def input(key):
    if key == 'escape':
        application.quit()
    
    # Pilih jenis blok
    if key == '1':  # Grass
        app.current_color = color.rgb(34, 139, 34)
        block_type_text.text = 'Block: Grass [1]'
    elif key == '2':  # Stone
        app.current_color = color.gray
        block_type_text.text = 'Block: Stone [2]'
    elif key == '3':  # Brick
        app.current_color = color.rgb(178, 34, 34)
        block_type_text.text = 'Block: Brick [3]'
    elif key == '4':  # Wood
        app.current_color = color.rgb(139, 69, 19)
        block_type_text.text = 'Block: Wood [4]'
    elif key == '5':  # Gold
        app.current_color = color.rgb(255, 215, 0)
        block_type_text.text = 'Block: Gold [5]'

print("\n" + "="*50)
print("GAME MINECRAFT-STYLE SIAP!")
print("="*50)
print("\nKONTROL:")
print("  WASD        : Bergerak")
print("  Mouse       : Lihat sekeliling")
print("  SPACE       : Lompat")
print("  KLIK KIRI   : Hancurkan blok")
print("  KLIK KANAN  : Tambah balok baru (arahkan ke balok lain)")
print("  1-5         : Pilih jenis blok")
print("  ESC         : Keluar")
print("\nCONTOH CARA MENAMBAH BALOK:")
print("  1. Pilih jenis balok (tekan 1-5)")
print("  2. Arahkan crosshair (+) ke balok yang ada")
print("  3. Klik kanan mouse")
print("  4. Balok baru muncul di sisi yang Anda klik!")
print("\nFITUR:")
print(f"  ✓ Pohon     : {len(tree_positions)} pohon di dunia")
print("  ✓ Rumah     : 1 rumah lengkap dengan atap")
print(f"  ✓ Total Blok: {len(blocks)} blok")
print("="*50 + "\n")

app.run()