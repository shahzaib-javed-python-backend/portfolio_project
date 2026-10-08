<div align="center">

# 🚀 Shahzaib Javed | Python Backend Engineer Portfolio

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11%25-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Django-5.x-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/Tailwind_CSS-3.8-38BDF8?style=for-the-badge&logo=tailwind-css&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Active-emerald?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Deployment-Vercel-black?style=for-the-badge&logo=vercel" />
</p>

> *A high-performance, SEO-optimized, terminal-themed developer portfolio and technical blogging platform built with Django and Tailwind CSS.*

</div>

---

## 💻 About The Project

This repository contains the source code for my personal developer portfolio and technical publication platform. Designed with a custom **Terminal/CLI aesthetics**, the application bridges high-speed backend execution with clean, responsive frontend architecture. 

It features an integrated CMS for long-form technical SEO articles, a secure asynchronous-ready contact dispatch system, and robust visitor analytics tracking.

---

## ✨ Core Features

* **Terminal UI / UX:** Immersive dark-mode developer aesthetic with interactive command cues (`$ start_project()`, `./connect.sh`).
* **High-Performance Blogging System:** Full CRUD structure with clean slug-based URLs, optimized for long-form technical articles (1500+ words) and organic search engine discovery.
* **Secure Contact Transmission:** Integrated Django messages framework with real-time success alerts and database persistence via custom admin panels.
* **Optimized Django Admin:** Tailored administrative dashboards for effortless content management, visitor tracking, and lead generation review.
* **Production-Ready Static Handling:** Configured with **WhiteNoise** for seamless static asset compression and delivery on serverless platforms.

---

## 🛠️ Tech Stack

* **Backend:** Python, Django (ASGI/WSGI)
* **Frontend:** Tailwind CSS, HTML5, JavaScript
* **Database:** SQLite (Development) / PostgreSQL-ready
* **Deployment & Hosting:** Vercel, Git, GitHub Actions

---

## 📂 Project Architecture

```text
portfolio_project/
│
├── core/                         # Main Django App
│   ├── migrations/               # Database migrations
│   ├── templates/core/           # Terminal UI & Blog templates
│   ├── admin.py                  # Custom admin panel registrations
│   ├── models.py                 # Blog, Contact, & Visitor models
│   ├── urls.py                   # App-level routing
│   └── views.py                  # Request handling & form processing
│
├── portfolio_project/            # Project Configuration
│   ├── settings.py               # Global settings & security config
│   ├── urls.py                   # Root URL dispatcher
│   └── wsgi.py                   # WSGI entry point for serverless deployment
│
├── static/                       # Compiled CSS & JS assets
├── manage.py                     # Django management utility
├── requirements.txt              # Project dependencies
└── vercel.json                   # Vercel serverless deployment config
