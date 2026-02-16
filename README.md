# Image Grayscale Converter with Performance Analysis

Projeto desenvolvido por **Larissa Campos Cardoso**  
GRVA – Uberlândia  

---

## Overview

This project implements a Python application capable of converting colored images to grayscale using three distinct pixel-based algorithms:

- Average Method  
- Luminosity Method (Weighted Average)  
- Desaturation Method  

The system also measures execution time for each method and allows graphical interaction through a Tkinter interface.

---

## Features

- Pixel-by-pixel grayscale conversion
- Performance timer for algorithm comparison
- Automatic image saving with method identification
- Simple graphical interface (Tkinter)
- Comparative analysis report (HTML → PDF)

---

## Project Structure

├── conversor_grayscale.py
├── relatorio_grayscale.html
├── README.md
└── analise_metodos.txt (optional)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```
### 2. Install dependencies

```bash
pip install pillow
```
Tkinter is included by default in most Python distributions.

### 3. Running the Application

```bash
python conversor_grayscale.py
```

---
## Steps:

- Select an image file.
- Choose one of the three grayscale methods.
- Click "Convert".
- The converted image will be displayed.
- The execution time will be shown.
- The image will be saved automatically in the project directory.

---

# Grayscale Conversion Methods
<details> <summary><strong>Average Method</strong></summary>

# Formula:

Gray = (R + G + B) / 3

# Characteristics:

Equal weight to all color channels
Simple implementation
Fast execution
May produce less realistic brightness

---

</details>
<details> <summary><strong>Luminosity Method</strong></summary>

# Formula:

Gray = 0.21R + 0.72G + 0.07B

# Characteristics:

Based on human visual perception
Higher weight for green channel
Produces more natural grayscale images
Slightly more computationally intensive

---

</details>
<details> <summary><strong>Desaturation Method</strong></summary>

# Formula:

Gray = (max(R,G,B) + min(R,G,B)) / 2

# Characteristics:

Uses contrast extremes
Preserves some contrast details
Mid-level computational cost

---

</details>
Performance Analysis
The execution time is measured using Python’s high-resolution timer (time.perf_counter()).

# General Observations:

Average method is typically the fastest.
Luminosity method produces the best visual quality.
Desaturation offers balanced contrast.
Differences in execution time are minimal for small images.
Larger images amplify performance differences.

---

# HTML Report Generation

The project includes an HTML file that generates a professional PDF report.

---

## To use it:

1. Open relatorio_grayscale.html in a browser.
2. Click "Gerar PDF".
3. The report will be downloaded automatically.

---

## The report includes:

- Project description
- Code explanation
- Comparison table
- Performance chart
- Author identification

---

## Technologies Used: 

Python 3
Pillow (PIL)
Tkinter
HTML5
CSS3
Chart.js
html2pdf.js

---

## Academic Context

This project was developed to analyze grayscale conversion techniques and compare computational efficiency and visual quality across different algorithms.

---

## It demonstrates:

1. Image processing fundamentals

2. Algorithm comparison

3. Report generation using web technologies

--
