import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

# 1. ขยายขนาดหน้าต่างภาพเป็น (14, 11) เพื่อเพิ่มพื้นที่
fig, axs = plt.subplots(3, 3, figsize=(14, 11))

# ตั้งชื่อภาพรวม พร้อมปรับตำแหน่งให้อยู่สูงขึ้นเล็กน้อย
fig.suptitle('My First Chart', fontsize=18, fontweight='bold', y=0.96)

# ----------------------------------------------------
# 1. Row 1, Col 1: Scatter Plot 1
x1 = np.random.randint(100, size=100)
y1 = np.random.randint(100, size=100)
colors1 = np.random.randint(100, size=100)
sc1 = axs[0, 0].scatter(x1, y1, c=colors1, s=15, cmap='cividis')
fig.colorbar(sc1, ax=axs[0, 0])
axs[0, 0].set_title('Scatter Plot 1', pad=10)
axs[0, 0].set_xlabel('X Label 1', labelpad=8)
axs[0, 0].set_ylabel('Y Label 1')

# 2. Row 1, Col 2: Scatter Plot 2
x2 = np.random.randint(100, size=50)
y2 = np.random.randint(100, size=50)
colors2 = np.random.randint(100, size=50)
sizes2 = 10 * np.random.randint(10, 100, size=50)
sc2 = axs[0, 1].scatter(x2, y2, c=colors2, s=sizes2, alpha=0.7, cmap='gist_earth')
fig.colorbar(sc2, ax=axs[0, 1])
axs[0, 1].set_title('Scatter Plot 2', pad=10)
axs[0, 1].set_xlabel('X Label 2', labelpad=8)
axs[0, 1].set_ylabel('Y Label 2')

# 3. Row 1, Col 3: Horizontal Bar Chart
x3 = np.array(["A", "B", "C", "D"])
y3 = np.array([3, 8, 1, 10])
axs[0, 2].barh(x3, y3, height=0.2, color='#1f77b4')
axs[0, 2].set_title('Horizontal Bar Chart', pad=10)
axs[0, 2].set_xlabel('X Label 3', labelpad=8)
axs[0, 2].set_ylabel('Y Label 3')

# ----------------------------------------------------
# 4. Row 2, Col 1: Sports Watch Data (ข้อ 4)
x4 = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y4 = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
axs[1, 0].plot(x4, y4, color='#1f77b4')
axs[1, 0].set_title('Sports Watch Data', pad=10)
axs[1, 0].set_xlabel('Average Pulse', labelpad=8)
axs[1, 0].set_ylabel('Calorie Burnage')
axs[1, 0].grid(color='green', linestyle='--', linewidth=0.5)  # ใส่เส้น grid สีเขียวเส้นประ

# 5. Row 2, Col 2: Zigzag Lines
y5_1 = np.array([3, 8, 1, 10])
y5_2 = np.array([6, 2, 7, 11])
axs[1, 1].plot(y5_1, color="#211fb4")
axs[1, 1].plot(y5_2, color="#b41f1f")
axs[1, 1].set_title('Zigzag Lines', pad=10)
axs[1, 1].set_xlabel('X Label 5', labelpad=8)
axs[1, 1].set_ylabel('Y Label 5')

# 6. Row 2, Col 3: Line with Markers
ypoints6 = np.array([3, 8, 1, 10])
axs[1, 2].plot(ypoints6, marker='o', ms=15, mfc='r', color='#1f77b4')
axs[1, 2].set_title('Line with Markers', pad=10)
axs[1, 2].set_xlabel('X Label 6', labelpad=8)
axs[1, 2].set_ylabel('Y Label 6')

# ----------------------------------------------------
# 7. Row 3, Col 1: Histogram
x7 = np.random.normal(170, 10, 250)
axs[2, 0].hist(x7, bins=10, color='#1f77b4')
axs[2, 0].set_title('Histogram', pad=10)
axs[2, 0].set_xlabel('X Label 7', labelpad=8)
axs[2, 0].set_ylabel('Y Label 7')

# 8. Row 3, Col 2: Pie Chart 1 (อัปเดตตามรูปที่ 8)
y8 = np.array([35, 25, 25, 15])
mylabels8 = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode8 = [0.2, 0, 0, 0]  # ดึง Apples ออกมา 0.2

axs[2, 1].pie(y8, labels=mylabels8, explode=myexplode8)
axs[2, 1].set_title('Pie Chart 1', pad=10)
axs[2, 1].set_xlabel('X Label 8', labelpad=8)
axs[2, 1].set_ylabel('Y Label 8')

# 9. Row 3, Col 3: Pie Chart 2 (Legend ย้ายตำแหน่งเพื่อไม่ให้บัง)
y9 = np.array([35, 25, 25, 15])
mylabels9 = ["Apples", "Bananas", "Cherries", "Dates"]
axs[2, 2].pie(y9, colors=['#1f77b4', '#8c564b', '#2ca02c', '#bcbd22'], startangle=90)
axs[2, 2].legend(mylabels9, loc='upper right', bbox_to_anchor=(1.15, 1), fontsize='small')
axs[2, 2].set_title('Pie Chart 2', pad=10)
axs[2, 2].set_xlabel('X Label 9', labelpad=8)
axs[2, 2].set_ylabel('Y Label 9')

# ----------------------------------------------------
# ปรับระยะห่างระหว่างแนวตั้ง (hspace) และแนวนอน (wspace) ให้กว้างขึ้น
plt.subplots_adjust(hspace=0.45, wspace=0.35, top=0.90, bottom=0.08, left=0.08, right=0.95)

# แสดงผล
plt.show()