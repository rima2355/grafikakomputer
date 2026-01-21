import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Inisialisasi variabel transformasi
tx, ty, tz = 0, 0, -10  # Translasi
rx, ry, rz = 0, 0, 0     # Rotasi
scale = 1.0              # Skala
reflect_x = 1            # Refleksi (1 normal, -1 terbalik)

def draw_cube(width, height, depth):
    """Menggambar kubus untuk badan rumah dengan dimensi custom"""
    w, h, d = width/2, height/2, depth/2
    
    vertices = [
        [w, -h, -d], [w, h, -d], [-w, h, -d], [-w, -h, -d],
        [w, -h, d], [w, h, d], [-w, -h, d], [-w, h, d]
    ]
    
    edges = [
        (0,1), (1,2), (2,3), (3,0),
        (4,5), (5,7), (7,6), (6,4),
        (0,4), (1,5), (2,7), (3,6)
    ]
    
    faces = [
        (0,1,2,3), (4,5,7,6), (0,1,5,4),
        (2,3,6,7), (0,3,6,4), (1,2,7,5)
    ]
    
    colors = [
        (0.9, 0.8, 0.6),  # Depan - Krem
        (0.85, 0.75, 0.55), # Belakang - Krem gelap
        (0.95, 0.85, 0.65), # Kanan - Krem terang
        (0.8, 0.7, 0.5),   # Kiri - Krem gelap
        (0.75, 0.65, 0.45), # Bawah
        (0.9, 0.8, 0.6)    # Atas
    ]
    
    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        glColor3fv(colors[i])
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()
    
    glColor3f(0.3, 0.3, 0.3)
    glLineWidth(2)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_roof(width, depth):
    """Menggambar atap berbentuk prisma segitiga (atap pelana)"""
    w, d = width/2, depth/2
    roof_height = width * 0.6  # Tinggi atap 60% dari lebar
    
    # Base atap (di atas rumah)
    base_height = width/2
    
    # Vertices atap
    # Front triangle
    front_left = [-w, base_height, d]
    front_right = [w, base_height, d]
    front_top = [0, base_height + roof_height, d]
    
    # Back triangle
    back_left = [-w, base_height, -d]
    back_right = [w, base_height, -d]
    back_top = [0, base_height + roof_height, -d]
    
    # Warna atap merah bata
    glColor3f(0.7, 0.2, 0.15)
    
    # Sisi depan
    glBegin(GL_TRIANGLES)
    glVertex3fv(front_left)
    glVertex3fv(front_right)
    glVertex3fv(front_top)
    glEnd()
    
    # Sisi belakang
    glBegin(GL_TRIANGLES)
    glVertex3fv(back_right)
    glVertex3fv(back_left)
    glVertex3fv(back_top)
    glEnd()
    
    # Sisi kiri atap
    glColor3f(0.6, 0.15, 0.1)
    glBegin(GL_QUADS)
    glVertex3fv(front_left)
    glVertex3fv(front_top)
    glVertex3fv(back_top)
    glVertex3fv(back_left)
    glEnd()
    
    # Sisi kanan atap
    glColor3f(0.65, 0.18, 0.12)
    glBegin(GL_QUADS)
    glVertex3fv(front_right)
    glVertex3fv(back_right)
    glVertex3fv(back_top)
    glVertex3fv(front_top)
    glEnd()
    
    # Garis tepi atap
    glColor3f(0.3, 0.1, 0.05)
    glLineWidth(2)
    glBegin(GL_LINE_LOOP)
    glVertex3fv(front_left)
    glVertex3fv(front_top)
    glVertex3fv(front_right)
    glEnd()
    
    glBegin(GL_LINE_LOOP)
    glVertex3fv(back_left)
    glVertex3fv(back_top)
    glVertex3fv(back_right)
    glEnd()
    
    glBegin(GL_LINES)
    glVertex3fv(front_left)
    glVertex3fv(back_left)
    glVertex3fv(front_right)
    glVertex3fv(back_right)
    glVertex3fv(front_top)
    glVertex3fv(back_top)
    glEnd()

def draw_door(width, height):
    """Menggambar pintu"""
    door_width = width * 0.15
    door_height = height * 0.35
    door_bottom = -height/2
    
    glColor3f(0.4, 0.25, 0.15)
    glBegin(GL_QUADS)
    glVertex3f(door_width, door_bottom, width/2 + 0.01)
    glVertex3f(door_width, door_bottom + door_height, width/2 + 0.01)
    glVertex3f(-door_width, door_bottom + door_height, width/2 + 0.01)
    glVertex3f(-door_width, door_bottom, width/2 + 0.01)
    glEnd()
    
    # Bingkai pintu
    glColor3f(0.2, 0.1, 0.05)
    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    glVertex3f(door_width, door_bottom, width/2 + 0.01)
    glVertex3f(door_width, door_bottom + door_height, width/2 + 0.01)
    glVertex3f(-door_width, door_bottom + door_height, width/2 + 0.01)
    glVertex3f(-door_width, door_bottom, width/2 + 0.01)
    glEnd()
    
    # Gagang pintu
    glColor3f(0.8, 0.7, 0.2)
    knob_x = door_width * 0.6
    knob_y = door_bottom + door_height * 0.5
    glPointSize(8)
    glBegin(GL_POINTS)
    glVertex3f(knob_x, knob_y, width/2 + 0.02)
    glEnd()

def draw_window(x, y, width):
    """Menggambar jendela"""
    w = width * 0.12
    
    # Kaca jendela
    glColor3f(0.6, 0.8, 1.0)
    glBegin(GL_QUADS)
    glVertex3f(x + w, y + w, width/2 + 0.01)
    glVertex3f(x + w, y - w, width/2 + 0.01)
    glVertex3f(x - w, y - w, width/2 + 0.01)
    glVertex3f(x - w, y + w, width/2 + 0.01)
    glEnd()
    
    # Bingkai jendela
    glColor3f(0.3, 0.2, 0.1)
    glLineWidth(4)
    glBegin(GL_LINE_LOOP)
    glVertex3f(x + w, y + w, width/2 + 0.01)
    glVertex3f(x + w, y - w, width/2 + 0.01)
    glVertex3f(x - w, y - w, width/2 + 0.01)
    glVertex3f(x - w, y + w, width/2 + 0.01)
    glEnd()
    
    # Garis tengah jendela (vertikal)
    glBegin(GL_LINES)
    glVertex3f(x, y + w, width/2 + 0.01)
    glVertex3f(x, y - w, width/2 + 0.01)
    # Garis tengah jendela (horizontal)
    glVertex3f(x + w, y, width/2 + 0.01)
    glVertex3f(x - w, y, width/2 + 0.01)
    glEnd()

def draw_house():
    """Menggambar rumah lengkap"""
    house_width = 3.0
    house_height = 2.5
    house_depth = 2.5
    
    # Badan rumah
    draw_cube(house_width, house_height, house_depth)
    
    # Atap
    draw_roof(house_width, house_depth)
    
    # Pintu
    draw_door(house_width, house_height)
    
    # Jendela
    window_y = house_height * 0.1
    draw_window(house_width * 0.35, window_y, house_width)  # Jendela kanan
    draw_window(-house_width * 0.35, window_y, house_width) # Jendela kiri

def draw_reflection():
    """Menggambar refleksi rumah (bayangan)"""
    glPushMatrix()
    glScalef(1, -0.5, 1)  # Refleksi terhadap sumbu Y
    glTranslatef(0, -4, 0)
    
    # Gambar rumah dengan transparansi
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glColor4f(0.5, 0.5, 0.5, 0.3)
    
    draw_house()
    
    glDisable(GL_BLEND)
    glPopMatrix()

def draw_background():
    """Menggambar background langit dan tanah dengan gradasi"""
    glDisable(GL_DEPTH_TEST)
    
    # Simpan matriks
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    
    # Background langit (gradasi biru)
    glBegin(GL_QUADS)
    # Atas (biru langit terang)
    glColor3f(0.4, 0.7, 1.0)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    # Bawah (biru langit lebih gelap)
    glColor3f(0.6, 0.85, 1.0)
    glVertex3f(1, 0, -1)
    glVertex3f(-1, 0, -1)
    glEnd()
    
    # Background tanah (gradasi hijau)
    glBegin(GL_QUADS)
    # Atas (hijau terang)
    glColor3f(0.4, 0.8, 0.3)
    glVertex3f(-1, 0, -1)
    glVertex3f(1, 0, -1)
    # Bawah (hijau lebih gelap)
    glColor3f(0.2, 0.5, 0.2)
    glVertex3f(1, -1, -1)
    glVertex3f(-1, -1, -1)
    glEnd()
    
    # Restore matriks
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
    
    glEnable(GL_DEPTH_TEST)

def draw_sun():
    """Menggambar matahari"""
    glPushMatrix()
    glTranslatef(6, 6, -8)
    glColor3f(1.0, 1.0, 0.3)
    
    # Matahari (menggunakan segitiga untuk membuat lingkaran)
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, 0, 0)
    for i in range(21):
        angle = i * 2 * math.pi / 20
        x = math.cos(angle) * 0.8
        y = math.sin(angle) * 0.8
        glVertex3f(x, y, 0)
    glEnd()
    glPopMatrix()

def draw_clouds():
    """Menggambar awan"""
    def draw_cloud(x, y, z):
        glPushMatrix()
        glTranslatef(x, y, z)
        glColor3f(1.0, 1.0, 1.0)
        
        # Awan terdiri dari beberapa lingkaran
        positions = [(0, 0), (-0.3, -0.1), (0.3, -0.1), (-0.15, 0.2), (0.15, 0.2)]
        for px, py in positions:
            glBegin(GL_TRIANGLE_FAN)
            glVertex3f(px, py, 0)
            for i in range(21):
                angle = i * 2 * math.pi / 20
                x_c = math.cos(angle) * 0.25
                y_c = math.sin(angle) * 0.25
                glVertex3f(px + x_c, py + y_c, 0)
            glEnd()
        glPopMatrix()
    
    draw_cloud(-4, 5, -7)
    draw_cloud(3, 6, -8)
    draw_cloud(-2, 7, -9)

def draw_grid():
    """Menggambar grid lantai"""
    glColor3f(0.3, 0.6, 0.25)
    glBegin(GL_LINES)
    for i in range(-10, 11):
        glVertex3f(i, -1.5, -10)
        glVertex3f(i, -1.5, 10)
        glVertex3f(-10, -1.5, i)
        glVertex3f(10, -1.5, i)
    glEnd()

def display_info(screen):
    """Menampilkan informasi kontrol"""
    font = pygame.font.Font(None, 24)
    texts = [
        "=== KONTROL TRANSFORMASI 3D ===",
        f"TRANSLASI (X,Y,Z): ({tx:.1f}, {ty:.1f}, {tz:.1f})",
        "  Arrow Keys: Geser X,Z | PgUp/PgDn: Geser Y",
        f"ROTASI (X,Y,Z): ({rx:.0f}, {ry:.0f}, {rz:.0f})",
        "  A/D: Rotasi Y | W/S: Rotasi X | Q/E: Rotasi Z",
        f"SKALA: {scale:.2f}x",
        "  +/-: Perbesar/Kecilkan",
        f"REFLEKSI: {'AKTIF (Terbalik)' if reflect_x == -1 else 'NORMAL'}",
        "  R: Toggle Refleksi X",
        "",
        "SPACE: Reset | ESC: Keluar"
    ]
    
    y = 10
    for text in texts:
        color = (255, 255, 0) if "===" in text else (255, 255, 255)
        surface = font.render(text, True, color)
        screen.blit(surface, (10, y))
        y += 25

def main():
    global tx, ty, tz, rx, ry, rz, scale, reflect_x
    
    pygame.init()
    display = (1000, 700)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Visualisasi Rumah 3D - 4 Transformasi')
    
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0, 0, -10)
    glEnable(GL_DEPTH_TEST)
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_SPACE:
                    tx, ty, tz = 0, 0, -10
                    rx, ry, rz = 0, 0, 0
                    scale = 1.0
                    reflect_x = 1
        
        keys = pygame.key.get_pressed()
        
        # TRANSLASI
        if keys[K_LEFT]: tx -= 0.1
        if keys[K_RIGHT]: tx += 0.1
        if keys[K_UP]: tz += 0.1
        if keys[K_DOWN]: tz -= 0.1
        if keys[K_PAGEUP]: ty += 0.1
        if keys[K_PAGEDOWN]: ty -= 0.1
        
        # ROTASI
        if keys[K_w]: rx += 2
        if keys[K_s]: rx -= 2
        if keys[K_a]: ry += 2
        if keys[K_d]: ry -= 2
        if keys[K_q]: rz += 2
        if keys[K_e]: rz -= 2
        
        # SKALA
        if keys[K_PLUS] or keys[K_EQUALS]: 
            scale = min(scale + 0.02, 3.0)
        if keys[K_MINUS]: 
            scale = max(scale - 0.02, 0.2)
        
        # REFLEKSI
        if keys[K_r]:
            pygame.time.wait(200)
            reflect_x *= -1
        
        # Render 3D
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Gambar background dulu (paling belakang)
        draw_background()
        draw_sun()
        draw_clouds()
        
        glPushMatrix()
        
        # Terapkan transformasi
        glTranslatef(tx, ty, tz)
        glRotatef(rx, 1, 0, 0)
        glRotatef(ry, 0, 1, 0)
        glRotatef(rz, 0, 0, 1)
        glScalef(scale * reflect_x, scale, scale)
        
        draw_grid()
        draw_house()
        draw_reflection()
        
        glPopMatrix()
        
        # Render 2D overlay
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        glOrtho(0, display[0], display[1], 0, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()
        glDisable(GL_DEPTH_TEST)
        
        # Buat surface untuk teks
        info_surface = pygame.Surface(display, pygame.SRCALPHA)
        display_info(info_surface)
        
        # Render teks ke OpenGL
        texture_data = pygame.image.tostring(info_surface, "RGBA", True)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glRasterPos2f(0, 0)
        glDrawPixels(display[0], display[1], GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
        glDisable(GL_BLEND)
        
        glPopMatrix()
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)
        glEnable(GL_DEPTH_TEST)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()