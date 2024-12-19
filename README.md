# IoT Management Platform

A powerful Django-based web application for managing IoT devices and objects. This platform provides a user-friendly interface for tracking, monitoring, and managing various IoT devices and their associated data. 🚀

## 📸 Screenshots

### Home Page
![Home Page](https://github.com/user-attachments/assets/42dcb574-c427-43db-b4b6-030565e70cc2)
*Modern and intuitive home page with key features and statistics*

### IoT Objects List
![Objects List](https://github.com/user-attachments/assets/57e7c4de-702d-4b1b-9b2d-c8066054dd76)
*Comprehensive list of connected objects with detailed information*

### Admin Dashboard
![Admin Dashboard](https://github.com/user-attachments/assets/4c051d7c-e14d-44d4-9e0a-609634279ec4)
*Powerful Django administration interface for managing the platform*

### Object Management
![Delete Object](https://github.com/user-attachments/assets/ba762f91-020b-47ee-af09-cfa530fd8075)
*Safe and secure object management with confirmation dialogs*

## ✨ Features

- 🔐 User authentication and authorization
- 💻 CRUD operations for IoT devices/objects
- 🎨 Modern and responsive user interface
- 📁 Static file management
- 🖼️ Template-based views
- 📝 Form handling and validation

## 🛠️ Technologies Used

- 🐍 Python 3.x
- 🎯 Django
- 🌐 HTML/CSS
- 🎨 Bootstrap
- 🗄️ SQLite (Database)
- 📂 Static Files Management

## 🏗️ Project Structure

```
IoT-Management-Platform/
├── GestionObjets/          # Main application directory
│   ├── migrations/         # Database migrations
│   ├── templates/         # Application templates
│   ├── forms.py          # Form definitions
│   ├── models.py         # Database models
│   ├── urls.py           # URL configurations
│   └── views.py          # View logic
├── static/                # Static files (CSS, JS, Images)
├── templates/             # Global templates
├── manage.py             # Django management script
└── requirements.txt      # Project dependencies
```

## 🚀 Setup Instructions

1. 📥 Clone the repository:
   ```bash
   git clone https://github.com/Moutabir-omar/IoT-Management-Platform.git
   cd IoT-Management-Platform
   ```

2. 🔧 Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. 📦 Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. 🗄️ Run migrations:
   ```bash
   python manage.py migrate
   ```

5. 👑 Create a superuser (admin):
   ```bash
   python manage.py createsuperuser
   ```

6. 🚀 Run the development server:
   ```bash
   python manage.py runserver
   ```

7. 🌐 Access the application at `http://localhost:8000`

## 🤝 Contributing

1. 🔱 Fork the repository
2. 🌿 Create your feature branch (`git checkout -b feature/YourFeature`)
3. 💾 Commit your changes (`git commit -m 'Add some feature'`)
4. 📤 Push to the branch (`git push origin feature/YourFeature`)
5. 🎯 Create a new Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

- **Omar Moutabir** - [GitHub Profile](https://github.com/Moutabir-omar)

## 🌟 Support

Give a ⭐️ if you like this project! 
