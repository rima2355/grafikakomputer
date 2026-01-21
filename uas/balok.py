from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

# Texture sederhana untuk blok
grass_texture = 'grass'
stone_texture = 'brick'
brick_texture = 'brick'
dirt_texture = 'brick'

# Kelas untuk setiap blok
class Voxel(Button):
    def __init__(self, position=(0,0,0), texture='white_cube'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            highlight_color=color.lime,
        )
    
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                # Hancurkan blok
                destroy(self)
            
            if key == 'right mouse down':
                # Buat blok baru di atas blok yang diklik
                Voxel(position=self.position + mouse.normal, texture=grass_texture)

# Kelas untuk pohon
class Tree(Entity):
    def __init__(self, position):
        super().__init__()
        # Batang pohon
        for i in range(4):
            Voxel(position=(position[0], i, position[2]), texture=brick_texture)
        
        # Daun pohon
        for x in range(-2, 3):
            for z in range(-2, 3):
                for y in range(4, 7):
                    if random.random() > 0.3:
                        v = Voxel(position=(position[0]+x, y, position[2]+z), texture=grass_texture)
                        v.color = color.green

# Buat ground (tanah)
print("Membuat dunia...")
for z in range(-20, 20):
    for x in range(-20, 20):
        # Layer rumput
        voxel = Voxel(position=(x, 0, z))
        voxel.texture = grass_texture
        voxel.color = color.color(0, 0.5, random.uniform(0.9, 1))
        
        # Tambahkan variasi ketinggian
        if random.random() < 0.05:
            # Buat bukit kecil
            height = random.randint(1, 3)
            for h in range(1, height):
                Voxel(position=(x, h, z), texture=dirt_texture)

# Buat beberapa pohon
print("Menanam pohon...")
tree_positions = []
for i in range(10):
    x = random.randint(-15, 15)
    z = random.randint(-15, 15)
    if (x, z) not in tree_positions:
        tree_positions.append((x, z))
        Tree((x, 1, z))

# Buat rumah sederhana
print("Membangun rumah...")
house_x, house_z = 10, 10

# Lantai rumah
for x in range(house_x, house_x + 6):
    for z in range(house_z, house_z + 6):
        Voxel(position=(x, 1, z), texture=stone_texture)

# Dinding rumah
for x in range(house_x, house_x + 6):
    for y in range(2, 5):
        # Dinding depan dan belakang
        Voxel(position=(x, y, house_z), texture=brick_texture)
        Voxel(position=(x, y, house_z + 5), texture=brick_texture)

for z in range(house_z + 1, house_z + 5):
    for y in range(2, 5):
        # Dinding kiri dan kanan
        Voxel(position=(house_x, y, z), texture=brick_texture)
        Voxel(position=(house_x + 5, y, z), texture=brick_texture)

# Atap rumah
roof_color = color.red
for x in range(house_x - 1, house_x + 7):
    for z in range(house_z - 1, house_z + 7):
        v = Voxel(position=(x, 5, z), texture=brick_texture)
        v.color = roof_color

# Pintu (hapus beberapa blok)
for y in range(2, 4):
    v = Voxel(position=(house_x + 2, y, house_z), texture=brick_texture)
    destroy(v)

# Player (First Person Controller)
player = FirstPersonController()
player.position = (0, 5, 0)
player.speed = 5
player.gravity = 0.5

# Sky
sky = Sky()
sky.color = color.rgb(135, 206, 235)

# UI Text
info_text = Text(
    text='Minecraft-Style Game\nKlik Kiri: Hancurkan Blok | Klik Kanan: Buat Blok\nWASD: Gerak | Mouse: Lihat | SPACE: Lompat | ESC: Keluar',
    position=(-0.85, 0.45),
    scale=1,
    origin=(0, 0),
    background=True
)

# Crosshair
crosshair = Entity(
    parent=camera.ui,
    model='quad',
    color=color.white,
    scale=0.008,
    rotation_z=45
)

# Mode selection
class BlockSelector(Entity):
    def __init__(self):
        super().__init__(parent=camera.ui)
        self.current_texture = grass_texture
        self.textures = [grass_texture, stone_texture, brick_texture, dirt_texture]
        self.index = 0
        
        self.indicator = Text(
            parent=self,
            text=f'Block: Grass (1)',
            position=(0.6, -0.45),
            scale=1.5,
            background=True
        )
    
    def input(self, key):
        if key == '1':
            self.index = 0
            self.current_texture = grass_texture
            self.indicator.text = 'Block: Grass (1)'
        elif key == '2':
            self.index = 1
            self.current_texture = stone_texture
            self.indicator.text = 'Block: Stone (2)'
        elif key == '3':
            self.index = 2
            self.current_texture = brick_texture
            self.indicator.text = 'Block: Brick (3)'
        elif key == '4':
            self.index = 3
            self.current_texture = dirt_texture
            self.indicator.text = 'Block: Dirt (4)'

block_selector = BlockSelector()

# Override Voxel untuk menggunakan texture yang dipilih
original_voxel_init = Voxel.__init__

def new_voxel_init(self, position=(0,0,0), texture='white_cube'):
    if texture == grass_texture and hasattr(block_selector, 'current_texture'):
        texture = block_selector.current_texture
    original_voxel_init(self, position, texture)

Voxel.__init__ = new_voxel_init

# Update fungsi input untuk menggunakan texture yang dipilih
def voxel_input_override(self, key):
    if self.hovered:
        if key == 'left mouse down':
            destroy(self)
        
        if key == 'right mouse down':
            texture = block_selector.current_texture if hasattr(block_selector, 'current_texture') else grass_texture
            new_voxel = Button(
                parent=scene,
                position=self.position + mouse.normal,
                model='cube',
                origin_y=0.5,
                texture=texture,
                color=color.color(0, 0, random.uniform(0.9, 1)),
                highlight_color=color.lime,
            )
            new_voxel.input = lambda key: voxel_input_override(new_voxel, key)

Voxel.input = voxel_input_override

def update():
    # Info posisi player
    info_text.text = f'Minecraft-Style Game | Pos: ({int(player.x)}, {int(player.y)}, {int(player.z)})\nKlik Kiri: Hancurkan | Klik Kanan: Buat | WASD: Gerak | SPACE: Lompat\n1-4: Pilih Blok | ESC: Keluar'

def input(key):
    if key == 'escape':
        application.quit()

print("Game siap! Selamat bermain!")
print("\nKONTROL:")
print("- WASD: Bergerak")
print("- Mouse: Lihat sekeliling")
print("- SPACE: Lompat")
print("- Klik Kiri: Hancurkan blok")
print("- Klik Kanan: Buat blok")
print("- 1-4: Pilih jenis blok")
print("- ESC: Keluar")

app.run()