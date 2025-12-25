import pygame
import math
import random
import sys

# Inisialisasi Pygame
try:
    pygame.init()
    print("Pygame berhasil diinisialisasi!")
except Exception as e:
    print(f"Error inisialisasi pygame: {e}")
    sys.exit(1)

# Konstanta
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 250)
NIGHT_SKY = (25, 25, 112)
SUNSET_SKY = (255, 140, 0)
SUN_YELLOW = (255, 220, 0)
MOON_WHITE = (230, 230, 250)
GRASS_GREEN = (34, 139, 34)
DARK_GRASS = (20, 80, 20)
MOUNTAIN_GRAY = (120, 120, 120)
TREE_BROWN = (101, 67, 33)
TREE_GREEN = (0, 128, 0)
WATER_BLUE = (64, 164, 223)
DARK_WATER = (30, 80, 120)
HOUSE_RED = (178, 34, 34)
CLOUD_WHITE = (240, 248, 255)
STAR_YELLOW = (255, 255, 150)

# Setup display
try:
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mini Scene - Siklus Siang Malam | Grafika Komputer")
    clock = pygame.time.Clock()
    print("Display berhasil dibuat!")
except Exception as e:
    print(f"Error membuat display: {e}")
    sys.exit(1)

# ============= ALGORITMA GRAFIKA KOMPUTER =============

# 1. ALGORITMA DDA
def draw_line_dda(surface, color, x1, y1, x2, y2):
    """Algoritma DDA untuk menggambar garis"""
    try:
        dx = x2 - x1
        dy = y2 - y1
        
        steps = int(max(abs(dx), abs(dy)))
        
        if steps == 0:
            return
        
        x_inc = dx / steps
        y_inc = dy / steps
        
        x, y = x1, y1
        
        for _ in range(steps):
            if 0 <= int(x) < WIDTH and 0 <= int(y) < HEIGHT:
                surface.set_at((int(x), int(y)), color)
            x += x_inc
            y += y_inc
    except:
        pass

# 2. ALGORITMA MIDPOINT CIRCLE
def draw_circle_midpoint(surface, color, xc, yc, radius):
    """Algoritma Midpoint Circle"""
    try:
        if radius <= 0:
            return
            
        x = 0
        y = int(radius)
        p = 1 - radius
        
        def safe_set_pixel(px, py):
            if 0 <= px < WIDTH and 0 <= py < HEIGHT:
                surface.set_at((px, py), color)
        
        # Plot 8 symmetric points
        safe_set_pixel(xc + x, yc + y)
        safe_set_pixel(xc - x, yc + y)
        safe_set_pixel(xc + x, yc - y)
        safe_set_pixel(xc - x, yc - y)
        safe_set_pixel(xc + y, yc + x)
        safe_set_pixel(xc - y, yc + x)
        safe_set_pixel(xc + y, yc - x)
        safe_set_pixel(xc - y, yc - x)
        
        while x < y:
            x += 1
            if p < 0:
                p += 2 * x + 1
            else:
                y -= 1
                p += 2 * (x - y) + 1
            
            safe_set_pixel(xc + x, yc + y)
            safe_set_pixel(xc - x, yc + y)
            safe_set_pixel(xc + x, yc - y)
            safe_set_pixel(xc - x, yc - y)
            safe_set_pixel(xc + y, yc + x)
            safe_set_pixel(xc - y, yc + x)
            safe_set_pixel(xc + y, yc - x)
            safe_set_pixel(xc - y, yc - x)
    except:
        pass

# 3. ALGORITMA POLIGON
def draw_polygon_outline(surface, color, points):
    """Menggambar outline poligon dengan DDA"""
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]
        draw_line_dda(surface, color, int(x1), int(y1), int(x2), int(y2))

# 4. TRANSFORMASI GEOMETRIS
def translate(points, tx, ty):
    """Translasi"""
    return [(x + tx, y + ty) for x, y in points]

def rotate(points, cx, cy, angle):
    """Rotasi"""
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    result = []
    for x, y in points:
        x_temp = x - cx
        y_temp = y - cy
        x_new = x_temp * cos_a - y_temp * sin_a
        y_new = x_temp * sin_a + y_temp * cos_a
        result.append((x_new + cx, y_new + cy))
    return result

# ============= OBJEK SCENE =============

def draw_sun(surface, x, y):
    """Matahari dengan Midpoint Circle (Translasi)"""
    # Body
    pygame.draw.circle(surface, SUN_YELLOW, (int(x), int(y)), 30)
    draw_circle_midpoint(surface, (255, 180, 0), int(x), int(y), 30)
    
    # Rays dengan DDA
    for i in range(12):
        angle = (2 * math.pi / 12) * i
        x1 = x + math.cos(angle) * 35
        y1 = y + math.sin(angle) * 35
        x2 = x + math.cos(angle) * 50
        y2 = y + math.sin(angle) * 50
        draw_line_dda(surface, SUN_YELLOW, int(x1), int(y1), int(x2), int(y2))

def draw_moon(surface, x, y):
    """Bulan dengan Midpoint Circle (Translasi)"""
    pygame.draw.circle(surface, MOON_WHITE, (int(x), int(y)), 28)
    draw_circle_midpoint(surface, (200, 200, 220), int(x), int(y), 28)
    
    # Craters
    pygame.draw.circle(surface, (180, 180, 200), (int(x - 8), int(y - 5)), 6)
    pygame.draw.circle(surface, (180, 180, 200), (int(x + 7), int(y + 8)), 5)
    pygame.draw.circle(surface, (180, 180, 200), (int(x + 5), int(y - 10)), 4)

def draw_star(surface, x, y, size):
    """Bintang dengan Midpoint Circle"""
    pygame.draw.circle(surface, STAR_YELLOW, (int(x), int(y)), int(size))
    draw_circle_midpoint(surface, WHITE, int(x), int(y), int(size))

def draw_mountain(surface, x, y, width, height, brightness):
    """Gunung dengan Poligon"""
    base_gray = int(120 * brightness)
    color = (base_gray, base_gray, base_gray)
    
    mountain = [
        (x, y),
        (x + width // 2, y - height),
        (x + width, y)
    ]
    pygame.draw.polygon(surface, color, mountain)
    
    outline_gray = int(80 * brightness)
    draw_polygon_outline(surface, (outline_gray, outline_gray, outline_gray), mountain)
    
    # Snow peak
    snow_brightness = int(255 * brightness)
    snow = [
        (x + width // 2, y - height),
        (x + width // 2 - 15, y - height + 30),
        (x + width // 2 + 15, y - height + 30)
    ]
    pygame.draw.polygon(surface, (snow_brightness, snow_brightness, snow_brightness), snow)

def draw_tree(surface, x, y, scale_f, brightness, leaf_color_index=0):
    """Pohon dengan Poligon + Skala"""
    # Warna daun berdasarkan musim virtual
    leaf_colors = [
        (0, int(128 * brightness), 0),  # Hijau
        (int(200 * brightness), int(200 * brightness), 0),  # Kuning
        (int(220 * brightness), int(120 * brightness), 0),  # Orange
        (int(150 * brightness), int(75 * brightness), 0)  # Coklat
    ]
    leaf_color = leaf_colors[leaf_color_index % 4]
    outline_color = (
        int(leaf_color[0] * 0.7),
        int(leaf_color[1] * 0.7),
        int(leaf_color[2] * 0.7)
    )
    
    # Trunk
    trunk_w = int(10 * scale_f)
    trunk_h = int(40 * scale_f)
    trunk_color = (int(101 * brightness), int(67 * brightness), int(33 * brightness))
    pygame.draw.rect(surface, trunk_color, (x - trunk_w//2, y - trunk_h, trunk_w, trunk_h))
    
    # Leaves (triangle)
    leaf_size = int(30 * scale_f)
    
    for i in range(3):
        offset = i * int(15 * scale_f)
        leaves = [
            (x, y - trunk_h - int(25 * scale_f) - offset),
            (x - leaf_size, y - trunk_h + int(5 * scale_f) - offset),
            (x + leaf_size, y - trunk_h + int(5 * scale_f) - offset)
        ]
        pygame.draw.polygon(surface, leaf_color, leaves)
        draw_polygon_outline(surface, outline_color, leaves)

def draw_house(surface, x, y, brightness, smoke_particles=None):
    """Rumah dengan Poligon"""
    # Body
    house_color = (int(178 * brightness), int(34 * brightness), int(34 * brightness))
    pygame.draw.rect(surface, house_color, (x, y - 60, 80, 60))
    
    # Roof
    roof_color = (int(101 * brightness), int(67 * brightness), int(33 * brightness))
    roof = [(x - 5, y - 60), (x + 40, y - 100), (x + 85, y - 60)]
    pygame.draw.polygon(surface, roof_color, roof)
    outline_color = (int(70 * brightness), int(50 * brightness), int(20 * brightness))
    draw_polygon_outline(surface, outline_color, roof)
    
    # Door
    door_color = (int(80 * brightness), int(50 * brightness), int(20 * brightness))
    pygame.draw.rect(surface, door_color, (x + 30, y - 35, 20, 35))
    
    # Window (berubah kuning saat malam)
    if brightness < 0.4:  # Malam - lampu menyala
        window_color = (255, 255, 150)
    else:
        window_color = (int(200 * brightness), int(200 * brightness), int(150 * brightness))
    
    pygame.draw.rect(surface, window_color, (x + 10, y - 45, 15, 15))
    draw_line_dda(surface, door_color, x + 17, y - 45, x + 17, y - 30)
    draw_line_dda(surface, door_color, x + 10, y - 37, x + 25, y - 37)
    
    # Cerobong asap (hanya jika ada smoke_particles)
    if smoke_particles is not None and brightness < 0.6:
        chimney_color = (int(70 * brightness), int(35 * brightness), int(17 * brightness))
        pygame.draw.rect(surface, chimney_color, (x + 60, y - 100, 12, 15))
        pygame.draw.rect(surface, chimney_color, (x + 55, y - 105, 22, 5))

def draw_cloud(surface, x, y, scale_f, brightness):
    """Awan dengan Circle"""
    cloud_bright = int(240 * brightness)
    color = (cloud_bright, cloud_bright, min(255, cloud_bright + 15))
    
    r = int(20 * scale_f)
    pygame.draw.circle(surface, color, (int(x - 25 * scale_f), int(y)), r)
    pygame.draw.circle(surface, color, (int(x), int(y - 8 * scale_f)), int(r * 1.2))
    pygame.draw.circle(surface, color, (int(x + 25 * scale_f), int(y)), r)

def draw_bird(surface, x, y, wing_angle, brightness):
    """Burung dengan DDA + Rotasi"""
    bird_color = (0, 0, 0) if brightness > 0.3 else (100, 100, 100)
    pygame.draw.circle(surface, bird_color, (int(x), int(y)), 3)
    offset = 8 + abs(int(wing_angle))
    draw_line_dda(surface, bird_color, int(x), int(y), int(x - 12), int(y - offset))
    draw_line_dda(surface, bird_color, int(x), int(y), int(x + 12), int(y - offset))

# ============= KELAS ANIMASI BARU =============

class MistParticle:
    """Partikel kabut untuk efek pagi/sore"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(3, 8)
        self.speed = random.uniform(0.2, 0.5)
        self.opacity = random.randint(50, 150)
        
    def update(self):
        self.x += random.uniform(-0.3, 0.3)
        self.y -= self.speed
        if self.y < 350 or self.x < 0 or self.x > WIDTH:
            self.y = random.randint(400, 450)
            self.x = random.randint(0, WIDTH)
            
    def draw(self, surface, brightness):
        # Buat surface transparan untuk efek alpha
        mist_surface = pygame.Surface((self.size*2, self.size*2), pygame.SRCALPHA)
        color = (200, 200, 220, int(self.opacity * brightness))
        pygame.draw.circle(mist_surface, color, (self.size, self.size), self.size)
        surface.blit(mist_surface, (int(self.x) - self.size, int(self.y) - self.size))

class FallingLeaf:
    """Daun jatuh dengan efek rotasi"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (random.randint(100, 150), random.randint(150, 200), 0)
        self.size = random.randint(4, 8)
        self.speed = random.uniform(0.5, 1.5)
        self.wind = random.uniform(-0.5, 0.5)
        self.rotation = random.uniform(0, math.pi*2)
        self.rot_speed = random.uniform(0.02, 0.05)
        
    def update(self):
        self.x += self.wind
        self.y += self.speed
        self.rotation += self.rot_speed
        
        if self.y > 500 or self.x < -50 or self.x > WIDTH + 50:
            self.y = random.randint(50, 150)
            self.x = random.randint(0, WIDTH)
            self.rotation = random.uniform(0, math.pi*2)
            
    def draw(self, surface, brightness):
        leaf_color = (
            int(self.color[0] * brightness),
            int(self.color[1] * brightness),
            int(self.color[2] * brightness)
        )
        
        # Buat surface untuk daun
        leaf_surface = pygame.Surface((self.size*3, self.size*3), pygame.SRCALPHA)
        
        # Gambar daun (oval)
        leaf_rect = pygame.Rect(self.size//2, self.size, self.size*2, self.size)
        pygame.draw.ellipse(leaf_surface, leaf_color, leaf_rect)
        
        # Rotasi
        rotated = pygame.transform.rotate(leaf_surface, math.degrees(self.rotation))
        surface.blit(rotated, (int(self.x) - rotated.get_width()//2, 
                              int(self.y) - rotated.get_height()//2))

class SmokeParticle:
    """Asap dari cerobong rumah"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(4, 10)
        self.speed = random.uniform(0.3, 0.8)
        self.opacity = random.randint(100, 200)
        self.drift = random.uniform(-0.5, 0.5)
        
    def update(self):
        self.x += self.drift
        self.y -= self.speed
        self.size -= 0.05
        self.opacity -= 2
        
        if self.opacity <= 0 or self.size <= 0:
            return False
        return True
        
    def draw(self, surface, brightness):
        if brightness < 0.6:  # Hanya tampil saat malam/sore
            # Buat surface transparan
            smoke_surface = pygame.Surface((int(self.size*2), int(self.size*2)), pygame.SRCALPHA)
            smoke_color = (100, 100, 100, int(self.opacity * brightness))
            pygame.draw.circle(smoke_surface, smoke_color, 
                             (int(self.size), int(self.size)), int(self.size))
            surface.blit(smoke_surface, (int(self.x) - int(self.size), int(self.y) - int(self.size)))

class StreetLight:
    """Lampu jalan dengan efek cahaya"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.light_intensity = 0
        self.light_pulse = 0
        
    def update(self, is_night):
        if is_night:
            self.light_pulse += 0.05
            self.light_intensity = 150 + int(math.sin(self.light_pulse) * 30)
        else:
            self.light_intensity = 0
            
    def draw(self, surface, is_night):
        # Tiang lampu
        pole_color = (100, 100, 100)
        pygame.draw.rect(surface, pole_color, (self.x - 3, self.y - 50, 6, 50))
        
        # Lampu
        if is_night and self.light_intensity > 0:
            # Efek cahaya (gradien)
            for i in range(10, 0, -1):
                radius = i * 4
                alpha = int(self.light_intensity * (i/10))
                
                # Buat surface untuk cahaya
                light_surface = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
                light_color = (255, 255, 150, alpha)
                pygame.draw.circle(light_surface, light_color, (radius, radius), radius)
                surface.blit(light_surface, (self.x - radius, self.y - 50 - radius))
            
            # Bohlam
            pygame.draw.circle(surface, (255, 255, 200), (self.x, self.y - 50), 8)

class WaterWave:
    """Gelombang air di danau"""
    def __init__(self):
        self.wave_offset = 0
        self.wave_speed = 0.05
        
    def update(self):
        self.wave_offset += self.wave_speed
        
    def draw(self, surface, y_level, brightness):
        wave_color = (
            int(40 * brightness),
            int(140 * brightness),
            int(200 * brightness)
        )
        
        # Gambar gelombang sinus kecil
        points = []
        for x in range(0, WIDTH, 2):
            wave_y = y_level + math.sin(x * 0.02 + self.wave_offset) * 2
            points.append((x, wave_y))
            
        if len(points) > 1:
            for i in range(len(points) - 1):
                x1, y1 = points[i]
                x2, y2 = points[i + 1]
                draw_line_dda(surface, wave_color, int(x1), int(y1), int(x2), int(y2))

class TwinklingStar:
    """Bintang dengan efek berkedip"""
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.base_size = size
        self.current_size = size
        self.twinkle_speed = random.uniform(0.02, 0.05)
        self.twinkle_offset = random.uniform(0, math.pi*2)
        self.twinkle_timer = 0
        
    def update(self):
        self.twinkle_timer += self.twinkle_speed
        self.current_size = self.base_size + math.sin(self.twinkle_timer + self.twinkle_offset) * 0.5
        
    def draw(self, surface):
        # Gambar bintang dengan ukuran berubah
        pygame.draw.circle(surface, STAR_YELLOW, (int(self.x), int(self.y)), int(self.current_size))
        draw_circle_midpoint(surface, WHITE, int(self.x), int(self.y), int(self.current_size))

class Firefly:
    """Kunang-kunang untuk suasana malam"""
    def __init__(self):
        self.x = random.randint(100, WIDTH-100)
        self.y = random.randint(200, 400)
        self.size = random.uniform(1.5, 3.0)
        self.speed_x = random.uniform(-0.5, 0.5)
        self.speed_y = random.uniform(-0.5, 0.5)
        self.glow_intensity = random.uniform(0.5, 1.0)
        self.glow_speed = random.uniform(0.03, 0.07)
        self.glow_timer = random.uniform(0, math.pi*2)
        
    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.glow_timer += self.glow_speed
        
        # Batasi pergerakan
        if self.x < 50 or self.x > WIDTH-50:
            self.speed_x *= -1
        if self.y < 200 or self.y > 450:
            self.speed_y *= -1
            
        # Perbarui intensitas cahaya
        self.glow_intensity = 0.5 + math.sin(self.glow_timer) * 0.5
        
    def draw(self, surface):
        # Efek cahaya kunang-kunang
        glow_size = int(self.size * (1 + self.glow_intensity * 0.5))
        glow_color = (255, 255, 150, int(150 * self.glow_intensity))
        
        # Buat surface untuk efek glow
        glow_surface = pygame.Surface((glow_size*2, glow_size*2), pygame.SRCALPHA)
        pygame.draw.circle(glow_surface, glow_color, (glow_size, glow_size), glow_size)
        surface.blit(glow_surface, (int(self.x) - glow_size, int(self.y) - glow_size))
        
        # Tubuh kunang-kunang
        body_color = (200, 200, 50)
        pygame.draw.circle(surface, body_color, (int(self.x), int(self.y)), int(self.size))

# ============= KELAS ANIMASI UTAMA =============

class DayNightCycle:
    def __init__(self):
        self.time = 0  # 0-1 (0=midnight, 0.5=noon, 1=midnight)
        self.speed = 0.0005# Kecepatan siklus
        
    def update(self):
        """Update waktu (Translasi temporal)"""
        self.time += self.speed
        if self.time >= 1.0:
            self.time = 0
    
    def get_sky_color(self):
        """Dapatkan warna langit berdasarkan waktu"""
        if self.time < 0.15:  # Malam awal
            return NIGHT_SKY
        elif self.time < 0.25:  # Fajar
            t = (self.time - 0.15) / 0.1
            return self.lerp_color(NIGHT_SKY, SUNSET_SKY, t)
        elif self.time < 0.35:  # Pagi
            t = (self.time - 0.25) / 0.1
            return self.lerp_color(SUNSET_SKY, SKY_BLUE, t)
        elif self.time < 0.65:  # Siang penuh
            return SKY_BLUE
        elif self.time < 0.75:  # Sore
            t = (self.time - 0.65) / 0.1
            return self.lerp_color(SKY_BLUE, SUNSET_SKY, t)
        elif self.time < 0.85:  # Sunset
            t = (self.time - 0.75) / 0.1
            return self.lerp_color(SUNSET_SKY, NIGHT_SKY, t)
        else:  # Malam
            return NIGHT_SKY
    
    def lerp_color(self, color1, color2, t):
        """Linear interpolation antara 2 warna"""
        return (
            int(color1[0] + (color2[0] - color1[0]) * t),
            int(color1[1] + (color2[1] - color1[1]) * t),
            int(color1[2] + (color2[2] - color1[2]) * t)
        )
    
    def get_sun_position(self):
        """
        Posisi matahari (Translasi melingkar PENUH)
        Matahari bergerak dari kiri ke kanan (full arc)
        """
        # Matahari aktif dari time 0.15 sampai 0.85 (siang penuh)
        if 0.15 <= self.time <= 0.85:
            # Normalize time ke range 0-1 untuk perjalanan matahari
            normalized = (self.time - 0.15) / (0.85 - 0.15)  # 0 to 1
            angle = math.pi * normalized  # 0 to π (setengah lingkaran)
            
            # Matahari bergerak dari kiri (0°) ke kanan (180°)
            x = WIDTH // 2 - math.cos(angle) * 380  # Mulai dari kiri
            y = 450 - math.sin(angle) * 280  # Naik ke atas
        else:
            # Matahari di bawah horizon (tidak terlihat)
            x = -100
            y = 600
        
        return (x, y)
    
    def get_moon_position(self):
        """
        Posisi bulan (Translasi melingkar PENUH)
        Bulan bergerak berlawanan dengan matahari (malam)
        """
        # Bulan aktif dari time 0.85 sampai 0.15 (lewat 0->1->0.15)
        if self.time >= 0.8 or self.time <= 0.2:
            if self.time >= 0.8:
                # Fase 1: dari 0.85 ke 1.0
                normalized = (self.time - 0.8) / (1.0 - 0.8)*0.5
            else:
                # Fase 2: dari 0.0 ke 0.15
                normalized = 0.5 + (self.time / 0.2) * 0.5
            
            angle = math.pi * normalized
            
            # Bulan bergerak dari kanan ke kiri
            x = WIDTH // 2 + math.cos(angle) * 380  # Mulai dari kanan
            y = 450 - math.sin(angle) * 280
        else:
            # Bulan di bawah horizon
            x = WIDTH + 100
            y = 600
        
        return (x, y)
    
    def get_brightness(self):
        """Kecerahan scene (0=gelap, 1=terang)"""
        if self.time < 0.15 or self.time > 0.85:
            return 0.2  # Malam
        elif self.time < 0.25:
            # Fajar: gelap ke terang
            return 0.2 + (self.time - 0.15) * 8
        elif self.time < 0.75:
            return 1.0  # Siang penuh
        elif self.time < 0.85:
            # Senja: terang ke gelap
            return 1.0 - (self.time - 0.75) * 8
        return 0.2
    
    def is_night(self):
        """Cek apakah malam"""
        return self.time < 0.15 or self.time > 0.85

class Cloud:
    def __init__(self, x, y, speed, scale):
        self.x = x
        self.y = y
        self.speed = speed
        self.scale = scale
    
    def update(self):
        """Translasi horizontal"""
        self.x += self.speed
        if self.x > WIDTH + 50:
            self.x = -50
    
    def draw(self, surface, brightness):
        draw_cloud(surface, self.x, self.y, self.scale, brightness)

class Bird:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.wing = 0
        self.wing_dir = 1
    
    def update(self):
        """Translasi + Rotasi sayap"""
        self.x += self.speed
        if self.x > WIDTH + 30:
            self.x = -30
        self.wing += self.wing_dir * 0.3
        if abs(self.wing) > 8:
            self.wing_dir *= -1
    
    def draw(self, surface, brightness):
        draw_bird(surface, self.x, self.y, self.wing, brightness)

class Windmill:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
    
    def update(self):
        """Rotasi baling-baling"""
        self.angle += 0.03
    
    def draw(self, surface, brightness):
        # Tower
        tower_color = (int(150 * brightness), int(75 * brightness), 0)
        pygame.draw.rect(surface, tower_color, (self.x - 8, self.y - 25, 16, 60))
        
        # Blades (rotation)
        blade_color = (int(240 * brightness), int(240 * brightness), int(240 * brightness))
        for i in range(4):
            angle = self.angle + (math.pi / 2) * i
            blade = [(0, 0), (6, 0), (6, 35), (0, 35)]
            rotated = rotate(blade, 3, 0, angle)
            translated = translate(rotated, self.x, self.y - 25)
            pygame.draw.polygon(surface, blade_color, translated)
            outline_color = (int(180 * brightness), int(180 * brightness), int(180 * brightness))
            draw_polygon_outline(surface, outline_color, translated)
        
        # Center
        center_color = (int(100 * brightness), int(50 * brightness), 0)
        pygame.draw.circle(surface, center_color, (self.x, self.y - 25), 6)

class Ripple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 0
        self.active = True
    
    def update(self):
        """Skala: membesar"""
        self.radius += 1
        if self.radius > 30:
            self.active = False
    
    def draw(self, surface, brightness):
        if self.active:
            water_color = (int(40 * brightness), int(140 * brightness), int(200 * brightness))
            draw_circle_midpoint(surface, water_color, int(self.x), int(self.y), int(self.radius))

# ============= MAIN =============

def main():
    print("Memulai game loop...")
    running = True
    
    # Day-Night Cycle
    day_night = DayNightCycle()
    
    # Objects yang sudah ada
    clouds = [Cloud(100, 80, 0.3, 0.8), Cloud(400, 60, 0.4, 1.0), Cloud(650, 90, 0.2, 0.9)]
    birds = [Bird(150, 120, 0.8), Bird(400, 140, 1.0)]
    windmill = Windmill(680, 420)
    ripples = []
    
    # Animasi baru
    mist_particles = [MistParticle(random.randint(0, WIDTH), random.randint(400, 450)) 
                     for _ in range(20)]
    falling_leaves = [FallingLeaf(random.randint(0, WIDTH), random.randint(50, 150)) 
                     for _ in range(15)]
    smoke_particles = []
    street_lights = [StreetLight(100, 400), StreetLight(250, 400), StreetLight(700, 400)]
    water_wave = WaterWave()
    
    # Kunang-kunang (hanya malam)
    fireflies = [Firefly() for _ in range(10)]
    
    # Bintang biasa
    stars = [(random.randint(50, WIDTH-50), random.randint(30, 200), random.uniform(1, 2.5)) 
             for _ in range(30)]
    
    # Bintang berkedip
    twinkling_stars = [TwinklingStar(sx, sy, size) for sx, sy, size in stars]
    
    # Variabel untuk perubahan warna daun
    leaf_color_timer = 0
    leaf_color_index = 0
    
    font = pygame.font.Font(None, 28)
    small_font = pygame.font.Font(None, 20)
    
    print("="*70)
    print("MINI SCENE - SIKLUS SIANG MALAM OTOMATIS (FULL CYCLE)")
    print("="*70)
    print("✅ MATAHARI: Terbit dari KIRI → Naik → Terbenam ke KANAN")
    print("✅ BULAN: Terbit dari KANAN → Naik → Terbenam ke KIRI")
    print("✅ Algoritma DDA (garis: sinar matahari, burung)")
    print("✅ Algoritma Midpoint Circle (matahari, bulan, bintang, riak)")
    print("✅ Algoritma Poligon (gunung, pohon, rumah, windmill)")
    print("✅ Transformasi Geometris:")
    print("   - Translasi: matahari/bulan bergerak PENUH, awan, burung")
    print("   - Rotasi: sayap burung, baling-baling windmill")
    print("   - Skala: riak air membesar, pohon berbeda ukuran")
    print("✅ ANIMASI BARU:")
    print("   - Kabut pagi/sore")
    print("   - Daun jatuh berputar")
    print("   - Asap dari cerobong")
    print("   - Lampu jalan berkedip")
    print("   - Gelombang air")
    print("   - Bintang berkedip")
    print("   - Kunang-kunang")
    print("\nKlik di danau untuk membuat riak air!")
    print("Tunggu dan lihat siklus siang-malam LENGKAP! ☀️🌙")
    print("="*70)
    
    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = event.pos
                    if 50 < mx < WIDTH - 50 and 400 < my < 480:
                        ripples.append(Ripple(mx, my))
            
            # Update waktu
            day_night.update()
            brightness = day_night.get_brightness()
            is_night = day_night.is_night()
            
            # Update perubahan warna daun (musim virtual)
            leaf_color_timer += 0.0001
            if leaf_color_timer > 0.2:
                leaf_color_index = (leaf_color_index + 1) % 4
                leaf_color_timer = 0
            
            # Update animasi baru
            water_wave.update()
            
            # Update kabut (hanya pagi dan sore)
            if 0.2 < day_night.time < 0.3 or 0.7 < day_night.time < 0.8:
                for mist in mist_particles:
                    mist.update()
            
            # Update daun jatuh
            for leaf in falling_leaves:
                leaf.update()
            
            # Update asap (hanya malam/sore)
            if brightness < 0.6 and random.random() < 0.1:
                smoke_particles.append(SmokeParticle(490, 340))  # Dari cerobong rumah
                
            for smoke in smoke_particles[:]:
                if not smoke.update():
                    smoke_particles.remove(smoke)
            
            # Update lampu jalan
            for light in street_lights:
                light.update(is_night)
            
            # Update kunang-kunang (hanya malam)
            if is_night:
                for firefly in fireflies:
                    firefly.update()
            
            # Update bintang berkedip
            if is_night:
                for star in twinkling_stars:
                    star.update()
            
            # Update objek yang sudah ada
            for cloud in clouds:
                cloud.update()
            
            if not is_night:  # Burung hanya siang
                for bird in birds:
                    bird.update()
            
            windmill.update()
            
            for ripple in ripples[:]:
                ripple.update()
                if not ripple.active:
                    ripples.remove(ripple)
            
            # ============= DRAWING =============
            
            # Background sky
            screen.fill(day_night.get_sky_color())
            
            # Bintang dan bintang berkedip (hanya malam)
            if is_night:
                for star in twinkling_stars:
                    star.draw(screen)
            
            # Sun and Moon
            sun_x, sun_y = day_night.get_sun_position()
            moon_x, moon_y = day_night.get_moon_position()
            
            # Gambar matahari jika di atas horizon
            if sun_y < 500:
                draw_sun(screen, sun_x, sun_y)
            
            # Gambar bulan jika di atas horizon
            if moon_y < 500:
                draw_moon(screen, moon_x, moon_y)
            
            # Kabut (hanya pagi dan sore)
            if 0.2 < day_night.time < 0.3 or 0.7 < day_night.time < 0.8:
                for mist in mist_particles:
                    mist.draw(screen, brightness)
            
            # Clouds
            for cloud in clouds:
                cloud.draw(screen, brightness)
            
            # Birds (only during day)
            if not is_night:
                for bird in birds:
                    bird.draw(screen, brightness)
            
            # Mountains
            draw_mountain(screen, 50, 400, 200, 150, brightness)
            draw_mountain(screen, 200, 400, 250, 180, brightness)
            draw_mountain(screen, 450, 400, 200, 130, brightness)
            
            # Ground
            grass_color = (
                int(34 * brightness),
                int(139 * brightness),
                int(34 * brightness)
            )
            pygame.draw.rect(screen, grass_color, (0, 400, WIDTH, 200))
            
            # Water
            water_color = (
                int(64 * brightness),
                int(164 * brightness),
                int(223 * brightness)
            )
            pygame.draw.rect(screen, water_color, (50, 400, WIDTH - 100, 80))
            
            # Gelombang air
            water_wave.draw(screen, 400, brightness)
            
            # Ripples dari klik
            for ripple in ripples:
                ripple.draw(screen, brightness)
            
            # Daun jatuh
            for leaf in falling_leaves:
                leaf.draw(screen, brightness)
            
            # Trees dengan warna daun berubah
            draw_tree(screen, 120, 400, 1.0, brightness, leaf_color_index)
            draw_tree(screen, 200, 400, 0.8, brightness, leaf_color_index)
            draw_tree(screen, 300, 400, 1.2, brightness, leaf_color_index)
            
            # House dengan asap
            draw_house(screen, 450, 400, brightness, smoke_particles)
            
            # Gambar asap
            for smoke in smoke_particles:
                smoke.draw(screen, brightness)
            
            # Windmill
            windmill.draw(screen, brightness)
            
            # Lampu jalan
            for light in street_lights:
                light.draw(screen, is_night)
            
            # Kunang-kunang (hanya malam)
            if is_night:
                for firefly in fireflies:
                    firefly.draw(screen)
            
            # UI
            time_of_day = ""
            if day_night.time < 0.15:
                time_of_day = "🌙 TENGAH MALAM"
            elif day_night.time < 0.25:
                time_of_day = "🌅 FAJAR"
            elif day_night.time < 0.4:
                time_of_day = "☀️ PAGI"
            elif day_night.time < 0.6:
                time_of_day = "☀️ SIANG"
            elif day_night.time < 0.75:
                time_of_day = "🌆 SORE"
            elif day_night.time < 0.85:
                time_of_day = "🌇 SENJA"
            else:
                time_of_day = "🌙 MALAM"
            
            # UI Background
            pygame.draw.rect(screen, (0, 0, 0, 180), (0, 0, WIDTH, 90))
            
            title = font.render("Mini Scene - Siklus Siang Malam (Full Cycle)", True, WHITE)
            time_text = font.render(time_of_day, True, (255, 255, 100))
            
            # Info posisi
            pos_info = small_font.render(f"Matahari: X={int(sun_x)}, Y={int(sun_y)} | Bulan: X={int(moon_x)}, Y={int(moon_y)}", 
                                        True, (150, 220, 255))
            info = small_font.render("Klik danau! | Kabut pagi/sore | Daun jatuh | Asap malam | Lampu jalan | Kunang-kunang", 
                                    True, (100, 200, 255))
            
            screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 8))
            screen.blit(time_text, (WIDTH // 2 - time_text.get_width() // 2, 35))
            screen.blit(pos_info, (WIDTH // 2 - pos_info.get_width() // 2, 58))
            screen.blit(info, (WIDTH // 2 - info.get_width() // 2, 75))
            
            pygame.display.flip()
            clock.tick(FPS)
    
    except Exception as e:
        print(f"Error di game loop: {e}")
        import traceback
        traceback.print_exc()
    
    print("Menutup pygame...")
    pygame.quit()
    print("Selesai!")

if __name__ == "__main__":
    main()