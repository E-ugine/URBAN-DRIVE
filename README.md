
# Urban Drive - Car Rental FullStack App

## Project Description

**Urban Drive** is a rental car website that allows users to browse available vehicles, make bookings, and manage rental services. Built with React for the frontend, Flask for the backend, and Sqlite for the database, this platform streamlines car rentals with modern technology, offering a smooth and reliable experience.



## Technologies Used

### Frontend:
- **React**: A JavaScript library for building dynamic user interfaces.
- **CSS**: Styling for all components, ensuring a clean and responsive design.

### Backend:
- **Flask**: A lightweight Python web framework for managing server-side requests and API development.
- **SQLAlchemy**: An ORM (Object Relational Mapper) used for database interactions.

### Database:
- **SQLite**: A lightweight relational database for managing car, user, payment, and booking data.

## Requirements
Before setting up the project, ensure you have the following installed:
- Python 3.8+
- Node.js 14+
- npm (Node Package Manager)
- Flask
-SQLITE3
- SQLAlchemy

### SETUP STEPS:
Clone the Repository:

1.Go to the repository URL: git clone https://github.com/E-ugine/urban-drive.git
2.Copy the SSH URL.
3.In your terminal, navigate to your preferred directory and run:
git clone <SSH URL>

###Installing Dependencies:

1.Open the cloned repository:
2.cd server/
3.Install required Python libraries using pip:
$ pipenv install 
$ pipenv shell


##Seed Data:
If needed, you can seed the database
  $ python seed.py


Run the Application:
-run it at port 5555. to set this if not yet set, after seeding your database,in the terminal run export FLASK_RUN_PORT=5555

##Start the Flask API:
flask run/ python app.py
    ```

### Frontend (React) Setup
1. Navigate to the frontend folder(client):
    ```bash
    cd client
    ```
2. Install the frontend dependencies:
    ```bash
    npm install
    ```
3. Start the React development server:
    ```bash
    npm start
    ```

## Usage Instructions
Once the servers are running, open your browser and go to `http://localhost:4000` to access the Urban Drive platform. From here, you can:
- Browse available cars.
- Sign up and log in to make bookings.
- Use the admin panel to manage cars and bookings.

## Documentation

### API Endpoints
- **GET /cars**: Retrieve a list of available cars.
- **POST /bookings**: Create a new booking.
- **GET /bookings**: View all bookings for a user.
- **PUT /admin/cars/:id**: Update car details (Admin).
- **DELETE /admin/cars/:id**: Remove a car from the list (Admin).

### Component Structure
- **App**: The main component that holds routing.
- **NavBar**: Displays navigation links.
- **CarList**: Lists all available cars.
- **CarDetails**: Displays details of a specific car.
- **BookingForm**: Handles booking creation.
- **AdminPanel**: Manages car listings and bookings.

## Support Information
If you encounter any issues, please feel free to open an issue on the GitHub repository. For direct inquiries, you can contact the development team at `agollaeugine@gmail.com`.

## Project Roadmap

Here are some future plans for Urban Drive:
1. ****: Enhance the user interface with advanced search options and visual improvements.
2. ****: Integrate payment gateways for online transactions.


## Contribution Guidelines

Contributions are welcome! Here's how you can contribute:
1. Fork the repository.
2. Create a new feature branch:
    ```bash
    git checkout -b feature/new-feature
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add new feature"
    ```
4. Push to the branch:
    ```bash
    git push origin feature/new-feature
    ```
5. Open a Pull Request.

Please ensure your code adheres to the style guidelines, and all tests pass before submitting.

## Acknowledgements
Special thanks to all the **Binary Brains** group members who contributed to making the Urban-Drive website feasible:
- **Eugine Owuor** (Scrum master)
- **Frankline Were**
- **Onesmus Odongo**
- **Roy Collins Nguithi**

And special thanks to the following resources and tools:
- **React Documentation**: For comprehensive tutorials and guidelines.
- **Flask Documentation**: For providing excellent resources for building web applications.
- **SQLAlchemy Documentation**: For ORM integration.

## License Information

This project is licensed under the **MIT License**. See the LICENSE file for more details.

## Conclusion

Urban Drive is a scalable and efficient platform designed for managing car rentals. With further development, we aim to provide a full-featured application ready for production deployment. Thank you for checking out the project, and we hope to collaborate with you!