# OvinoSul - Sheep Farming Website

## 🐑 Project Overview
OvinoSul is a professional static website dedicated to sheep farming in Rio Grande do Sul, Brazil. It provides comprehensive information about sheep breeds, vaccination schedules, and practical farming tips specifically tailored to the climate and conditions of the Rio Grande do Sul region.

## 📁 Project Structure
This is a **static HTML website** with no backend dependencies, consisting of:
- **Frontend**: HTML, CSS, JavaScript (vanilla JS)
- **Content Language**: Portuguese (Brazil)
- **Target Audience**: Sheep farmers and agriculture enthusiasts in Rio Grande do Sul

### Key Pages
- `index.html` - Main homepage with hero section and feature overview
- `racas.html` - Detailed profiles of sheep breeds
- `vacinas.html` - Vaccination calendar and schedules
- `demo-navigation.html` - Navigation demo page

## 🛠️ Technology Stack
- **HTML5**: Semantic markup with accessibility features
- **CSS3**: Modern styling with CSS custom properties, Grid, Flexbox
- **JavaScript**: Vanilla ES6+ with no external dependencies
- **PWA Features**: Service Worker (`sw.js`) and Web App Manifest
- **Responsive Design**: Mobile-first approach with multiple breakpoints

## 🚀 Development Setup
The project runs a simple Python static file server on port 5000:

### Workflow Configuration
- **Server**: Python HTTP server serving static files
- **Port**: 5000 (configured for Replit environment)
- **Host**: 0.0.0.0 (allows external access)
- **Cache**: Disabled during development for easier testing

### Recent Configuration Changes
- Fixed JavaScript error where header selector was incorrect
- Configured deployment for autoscale (static website)
- Added proper cache control headers

## 📱 Features
- **Progressive Web App**: Service worker for offline functionality
- **Responsive Design**: Optimized for mobile, tablet, and desktop
- **Search Functionality**: Built-in search across site content
- **Modern UI**: Professional design with smooth animations
- **Accessibility**: WCAG compliant with proper ARIA labels

## 🌐 Deployment
- **Type**: Static website (autoscale deployment)
- **Environment**: Production-ready with proper cache headers
- **Performance**: Optimized for fast loading and SEO

## 📊 Performance Considerations
- Lazy loading for images
- Optimized CSS and JavaScript
- Service worker caching for offline access
- Mobile-first responsive design

## 🔧 Maintenance
- All static assets are version controlled
- No database dependencies
- Service worker handles caching automatically
- Simple deployment process

---

**Project imported and configured for Replit environment on September 16, 2025**