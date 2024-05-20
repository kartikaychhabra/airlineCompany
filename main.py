import datetime

# User and Role Classes
class Role:
    PASSENGER = 'Passenger'
    STAFF = 'Staff'
    ADMIN = 'Admin'

class User:
    def __init__(self, user_id, surname, name, address, phone, role, password):
        self.user_id = user_id
        self.surname = surname
        self.name = name
        self.address = address
        self.phone = phone
        self.role = role
        self.password = password
        self.bookings = []
        if role == Role.PASSENGER:
            self.passenger = Passenger(user_id, surname, name, address, phone)
        elif role == Role.STAFF:
            self.staff = Staff(user_id, surname, name, address, phone, 0, role, None)
        else:
            self.passenger = None
            self.staff = None

    def update_profile(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        print(f"User {self.user_id} profile updated.")
        if self.role == Role.PASSENGER and self.passenger:
            self.passenger.update_profile(name, address, phone)
        elif self.role == Role.STAFF and self.staff:
            self.staff.update_personal_info(name, address, phone)

class Passenger:
    def __init__(self, passenger_id, surname, name, address, phone):
        self.passenger_id = passenger_id
        self.surname = surname
        self.name = name
        self.address = address
        self.phone = phone
        self.bookings = []

    def book_flight(self, flight):
        booking = Booking(self, flight)
        self.bookings.append(booking)
        print(f"Passenger {self.name} booked flight {flight.flight_num}.")
        return booking

    def update_profile(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        print(f"Passenger {self.passenger_id} profile updated.")

    def view_booking_history(self):
        print(f"Booking history for {self.name}: {[b.flight.flight_num for b in self.bookings]}")
        return self.bookings

    def view_details(self):
        details = {
            "Passenger ID": self.passenger_id,
            "Surname": self.surname,
            "Name": self.name,
            "Address": self.address,
            "Phone": self.phone,
            "Bookings": [booking.flight.flight_num for booking in self.bookings]
        }
        print(f"Passenger details: {details}")
        return details

class Booking:
    def __init__(self, passenger, flight):
        self.passenger = passenger
        self.flight = flight
        self.seat = None

    def cancel_booking(self):
        self.passenger.bookings.remove(self)
        self.flight.bookings.remove(self)
        print(f"Booking for flight {self.flight.flight_num} canceled.")

    def change_seat(self, new_seat):
        if new_seat in self.flight.available_seats:
            self.seat = new_seat
            print(f"Seat changed to {new_seat} for flight {self.flight.flight_num}.")
            return True
        print("Seat change failed.")
        return False

class Flight:
    def __init__(self, flight_num, origin, dest, date, arr_time, dep_time):
        self.flight_num = flight_num
        self.origin = origin
        self.dest = dest
        self.date = date
        self.arr_time = arr_time
        self.dep_time = dep_time
        self.bookings = []
        self.staff = []
        self.aircraft = None
        self.available_seats = set(range(1, 201))  # Assuming 200 seats per flight
        self.route = Route(origin, dest)

    def assign_staff(self, staff, role):
        flight_staff = FlightStaff(self, staff, role)
        self.staff.append(flight_staff)
        print(f"Staff {staff.name} assigned to flight {self.flight_num} as {role}.")
        return flight_staff

    def allocate_aircraft(self, airplane):
        self.aircraft = airplane
        print(f"Aircraft {airplane.serial_num} allocated to flight {self.flight_num}.")

    def update_status(self, new_status):
        self.status = new_status
        print(f"Flight {self.flight_num} status updated to {new_status}.")

    def add_intermediate_stop(self, city):
        self.route.add_intermediate_city(city)
        print(f"Added intermediate stop in {city.name} for flight {self.flight_num}.")

    def remove_intermediate_stop(self, city):
        self.route.remove_intermediate_city(city)
        print(f"Removed intermediate stop in {city.name} for flight {self.flight_num}.")

class FlightStaff:
    def __init__(self, flight, staff, role):
        self.flight = flight
        self.staff = staff
        self.role = role

    def change_role(self, new_role):
        self.role = new_role
        print(f"Staff role changed to {new_role} for flight {self.flight.flight_num}.")

class Airplane:
    def __init__(self, serial_num, manufacturer, model):
        self.serial_num = serial_num
        self.manufacturer = manufacturer
        self.model = model

    def schedule_maintenance(self, date):
        self.maintenance_date = date
        print(f"Maintenance scheduled for airplane {self.serial_num} on {date}.")

class Staff:
    def __init__(self, emp_num, surname, name, address, phone, salary, role, type_rating):
        self.emp_num = emp_num
        self.surname = surname
        self.name = name
        self.address = address
        self.phone = phone
        self.salary = salary
        self.role = role
        self.type_rating = type_rating

    def update_personal_info(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        print(f"Staff {self.emp_num} personal info updated.")

    def request_salary_change(self, new_salary):
        self.salary = new_salary
        print(f"Salary change requested to {new_salary} for staff {self.emp_num}.")

    def assign_type_rating(self, rating):
        self.type_rating = rating
        print(f"Type rating {rating} assigned to staff {self.emp_num}.")

class City:
    def __init__(self, city_id, name, airport):
        self.city_id = city_id
        self.name = name
        self.airport = airport
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)
        print(f"Flight {flight.flight_num} added to city {self.name}.")

    def remove_flight(self, flight):
        self.flights.remove(flight)
        print(f"Flight {flight.flight_num} removed from city {self.name}.")

class Route:
    def __init__(self, origin, dest):
        self.origin = origin
        self.dest = dest
        self.intermediate_cities = []

    def add_intermediate_city(self, city):
        self.intermediate_cities.append(city)
        print(f"Intermediate city {city.name} added to route from {self.origin} to {self.dest}.")

    def remove_intermediate_city(self, city):
        self.intermediate_cities.remove(city)
        print(f"Intermediate city {city.name} removed from route from {self.origin} to {self.dest}.")

class PassengerRepository:
    def __init__(self):
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)
        print(f"Passenger {passenger.name} added to repository.")

    def get_passenger(self, user_id):
        for user in self.passengers:
            if isinstance(user, User) and user.user_id == user_id:
                return user
        return None

class FlightRepository:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)
        print(f"Flight {flight.flight_num} added to repository.")

    def get_flight(self, flight_num):
        for flight in self.flights:
            if flight.flight_num == flight_num:
                return flight
        return None

class StaffRepository:
    def __init__(self):
        self.staff = []

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Staff {staff_member.name} added to repository.")

    def get_staff(self, emp_num):
        for user in self.staff:
            if isinstance(user, User) and user.user_id == emp_num:
                return user
        return None

class AirplaneRepository:
    def __init__(self):
        self.airplanes = []

    def add_airplane(self, airplane):
        self.airplanes.append(airplane)
        print(f"Airplane {airplane.serial_num} added to repository.")

    def get_airplane(self, serial_num):
        for airplane in self.airplanes:
            if airplane.serial_num == serial_num:
                return airplane
        return None

class CityRepository:
    def __init__(self):
        self.cities = []

    def add_city(self, city):
        self.cities.append(city)
        print(f"City {city.name} added to repository.")

    def get_city(self, city_id):
        for city in self.cities:
            if city.city_id == city_id:
                return city
        return None

    def remove_city(self, city):
        self.cities.remove(city)
        print(f"City {city.name} removed from repository.")

class PassengerController:
    def __init__(self, passenger_repository, flight_repository):
        self.passenger_repository = passenger_repository
        self.flight_repository = flight_repository

    def book_flight(self, user, flight_num):
        if user.role != Role.PASSENGER:
            print("Access denied: Only passengers can book flights.")
            return None
        passenger = self.passenger_repository.get_passenger(user.user_id)
        flight = self.flight_repository.get_flight(flight_num)
        if passenger and flight:
            booking = passenger.passenger.book_flight(flight)
            flight.bookings.append(booking)
            return booking
        return None

    def view_booking_history(self, user):
        if user.role != Role.PASSENGER:
            print("Access denied: Only passengers can view booking history.")
            return []
        passenger = self.passenger_repository.get_passenger(user.user_id)
        if passenger:
            return passenger.passenger.view_booking_history()
        return []

    def view_passenger_details(self, user):
        if user.role != Role.PASSENGER:
            print("Access denied: Only passengers can view details.")
            return {}
        passenger = self.passenger_repository.get_passenger(user.user_id)
        if passenger:
            return passenger.passenger.view_details()
        return {}

    def update_passenger_details(self, user, name, address, phone):
        if user.role != Role.PASSENGER:
            print("Access denied: Only passengers can update details.")
            return False
        passenger = self.passenger_repository.get_passenger(user.user_id)
        if passenger:
            passenger.passenger.update_profile(name, address, phone)
            return True
        return False

class StaffController:
    def __init__(self, flight_repository, staff_repository):
        self.flight_repository = flight_repository
        self.staff_repository = staff_repository

    def view_flight_details(self, user, flight_num):
        if user.role != Role.STAFF:
            print("Access denied: Only staff can view flight details.")
            return None
        flight = self.flight_repository.get_flight(flight_num)
        if flight:
            print(f"Flight details for flight {flight_num}: Origin {flight.origin}, Destination {flight.dest}, Date {flight.date}, Arrival Time {flight.arr_time}, Departure Time {flight.dep_time}.")
            return flight
        return None

    def assign_staff(self, user, flight_num, emp_num, role):
        if user.role != Role.STAFF and user.role != Role.ADMIN:
            print("Access denied: Only staff or admin can assign staff.")
            return None
        flight = self.flight_repository.get_flight(flight_num)
        staff_member = self.staff_repository.get_staff(emp_num)
        if flight and staff_member:
            assigned_staff = flight.assign_staff(staff_member.staff, role)
            print(f"Assigned staff {staff_member.surname} to flight {flight_num} as {role}.")
            return assigned_staff
        return None

    def track_certifications(self, user, emp_num):
        if user.role != Role.STAFF and user.role != Role.ADMIN:
            print("Access denied: Only staff or admin can track certifications.")
            return None
        staff_member = self.staff_repository.get_staff(emp_num)
        if staff_member:
            print(f"Certifications for {staff_member.surname}: {staff_member.staff.type_rating}")
            return staff_member.staff.type_rating
        return None

    def view_employee_details(self, user, emp_num):
        if user.role != Role.STAFF and user.role != Role.ADMIN:
            print("Access denied: Only staff or admin can view employee details.")
            return None
        staff_member = self.staff_repository.get_staff(emp_num)
        if staff_member:
            details = {
                "Employee ID": staff_member.user_id,
                "Surname": staff_member.surname,
                "Name": staff_member.name,
                "Address": staff_member.address,
                "Phone": staff_member.phone,
                "Role": staff_member.role,
                "Salary": staff_member.staff.salary,
                "Type Rating": staff_member.staff.type_rating
            }
            print(f"Employee details: {details}")
            return details
        return None

class AdminController:
    def __init__(self, flight_repository, airplane_repository, city_repository, passenger_repository, staff_repository):
        self.flight_repository = flight_repository
        self.airplane_repository = airplane_repository
        self.city_repository = city_repository
        self.passenger_repository = passenger_repository
        self.staff_repository = staff_repository

    def allocate_aircraft(self, user, flight_num, serial_num):
        if user.role != Role.ADMIN:
            print("Access denied: Only admin can allocate aircraft.")
            return None
        flight = self.flight_repository.get_flight(flight_num)
        airplane = self.airplane_repository.get_airplane(serial_num)
        if flight and airplane:
            flight.allocate_aircraft(airplane)
            return airplane
        return None

    def update_flight_status(self, user, flight_num, new_status):
        if user.role != Role.ADMIN:
            print("Access denied: Only admin can update flight status.")
            return None
        flight = self.flight_repository.get_flight(flight_num)
        if flight:
            flight.update_status(new_status)
            return flight
        return None

    def add_city(self, user, city):
        if user.role != Role.ADMIN:
            print("Access denied: Only admin can add cities.")
            return None
        self.city_repository.add_city(city)
        print(f"City {city.name} added.")
        return city

    def remove_city(self, user, city_id):
        if user.role != Role.ADMIN:
            print("Access denied: Only admin can remove cities.")
            return None
        city = self.city_repository.get_city(city_id)
        if city:
            self.city_repository.remove_city(city)
            print(f"City {city.name} removed.")
            return city
        else:
            print("City not found.")
            return None

    def update_city(self, user, city_id, new_name, new_airport):
        if user.role != Role.ADMIN:
            print("Access denied: Only admin can update cities.")
            return None
        city = self.city_repository.get_city(city_id)
        if city:
            city.name = new_name
            city.airport = new_airport
            print(f"City {city_id} updated to {new_name} with airport {new_airport}.")
            return city
        else:
            print("City not found.")
            return None

    def hire_employee(self, user, emp_num, surname, name, address, phone, salary, role, type_rating):
        if user.role != Role.ADMIN:
            print("Access denied: Only admin can hire employees.")
            return None
        staff_member = Staff(emp_num, surname, name, address, phone, salary, role, type_rating)
        self.staff_repository.add_staff(staff_member)
        print(f"Employee {name} hired.")
        return staff_member

    def update_employee(self, user, emp_num, name=None, address=None, phone=None, salary=None, type_rating=None):
        if user.role != Role.ADMIN:
            print("Access denied: Only admin can update employees.")
            return None
        staff_member = self.staff_repository.get_staff(emp_num)
        if staff_member:
            if name:
                staff_member.name = name
            if address:
                staff_member.address = address
            if phone:
                staff_member.phone = phone
            if salary:
                staff_member.salary = salary
            if type_rating:
                staff_member.type_rating = type_rating
            print(f"Employee {staff_member.surname} updated.")
            return staff_member
        else:
            print("Employee not found.")
            return None

    def manage_flight_route(self, user, flight_num, origin, dest, intermediate_cities=None):
        if user.role != Role.ADMIN:
            print("Access denied: Only admin can manage flight routes.")
            return None
        flight = self.flight_repository.get_flight(flight_num)
        if flight:
            flight.origin = origin
            flight.dest = dest
            if intermediate_cities:
                flight.route.intermediate_cities = intermediate_cities
            print(f"Flight {flight_num} route updated to origin: {origin}, destination: {dest}, intermediate cities: {intermediate_cities}.")
            return flight.route
        return None

    def schedule_flight(self, user, flight_num, date, arr_time, dep_time):
        if user.role != Role.ADMIN:
            print("Access denied: Only admin can schedule flights.")
            return None
        flight = self.flight_repository.get_flight(flight_num)
        if flight:
            flight.date = date
            flight.arr_time = arr_time
            flight.dep_time = dep_time
            print(f"Flight {flight_num} scheduled on {date} from {arr_time} to {dep_time}.")
            return flight
        return None

    def cancel_flight(self, user, flight_num):
        if user.role != Role.ADMIN:
            print("Access denied: Only admin can cancel flights.")
            return None
        flight = self.flight_repository.get_flight(flight_num)
        if flight:
            self.flight_repository.flights.remove(flight)
            print(f"Flight {flight_num} canceled.")
            return flight
        return None

    def add_airplane(self, user, serial_num, manufacturer, model):
        if user.role != Role.ADMIN:
            print("Access denied: Only admin can add airplanes.")
            return None
        airplane = Airplane(serial_num, manufacturer, model)
        self.airplane_repository.add_airplane(airplane)
        print(f"Airplane {serial_num} added.")
        return airplane

    def update_airplane(self, user, serial_num, manufacturer=None, model=None):
        if user.role != Role.ADMIN:
            print("Access denied: Only admin can update airplanes.")
            return None
        airplane = self.airplane_repository.get_airplane(serial_num)
        if airplane:
            if manufacturer:
                airplane.manufacturer = manufacturer
            if model:
                airplane.model = model
            print(f"Airplane {serial_num} updated.")
            return airplane
        return None

    def decommission_airplane(self, user, serial_num):
        if user.role != Role.ADMIN:
            print("Access denied: Only admin can decommission airplanes.")
            return None
        airplane = self.airplane_repository.get_airplane(serial_num)
        if airplane:
            self.airplane_repository.airplanes.remove(airplane)
            print(f"Airplane {serial_num} decommissioned.")
            return airplane
        return None

    def view_airplane_details(self, user, serial_num):
        if user.role != Role.ADMIN and user.role != Role.STAFF:
            print("Access denied: Only admin or staff can view airplane details.")
            return None
        airplane = self.airplane_repository.get_airplane(serial_num)
        if airplane:
            details = {
                "Serial Number": airplane.serial_num,
                "Manufacturer": airplane.manufacturer,
                "Model": airplane.model
            }
            print(f"Airplane details: {details}")
            return details
        return None

    def view_city_details(self, user, city_id):
        if user.role != Role.ADMIN:
            print("Access denied: Only admin can view city details.")
            return None
        city = self.city_repository.get_city(city_id)
        if city:
            details = {
                "City ID": city.city_id,
                "Name": city.name,
                "Airport": city.airport
            }
            print(f"City details: {details}")
            return details
        return None

    def get_all_passengers(self, user):
        if user.role != Role.ADMIN:
            print("Access denied: Only admin can view all passengers.")
            return None
        passengers = self.passenger_repository.passengers
        for passenger in passengers:
            if passenger.role == Role.PASSENGER:
                print(f"Passenger ID: {passenger.user_id}, Name: {passenger.name}, Address: {passenger.address}, Phone: {passenger.phone}")
        return passengers

def initialize_data():
    # Repositories
    passenger_repo = PassengerRepository()
    flight_repo = FlightRepository()
    staff_repo = StaffRepository()
    airplane_repo = AirplaneRepository()
    city_repo = CityRepository()

    # Controllers
    passenger_controller = PassengerController(passenger_repo, flight_repo)
    staff_controller = StaffController(flight_repo, staff_repo)
    admin_controller = AdminController(flight_repo, airplane_repo, city_repo, passenger_repo, staff_repo)

    # Sample Data
    admin = User(3, "Admin", "Super", "789 Pine St", "123123123", Role.ADMIN, "adminpass")
    passenger_repo.add_passenger(admin)  # Add the admin user to the passenger repository

    print("Contents of passenger_repo after adding admin user:")
    for user in passenger_repo.passengers:
        print(f"User ID: {user.user_id}, Name: {user.name}, Role: {user.role}")

    passenger = User(1, "Doe", "John", "123 Main St", "123456789", Role.PASSENGER, "pass123")
    passenger_repo.add_passenger(passenger)

    staff = User(2, "Smith", "Alice", "456 Birch St", "987654321", Role.STAFF, "staffpass")
    staff_repo.add_staff(staff)

    flight = Flight(1, "LHR", "JFK", datetime.date(2023, 6, 1), "10:00", "14:00")
    flight_repo.add_flight(flight)

    airplane = Airplane("1234", "Boeing", "737")
    airplane_repo.add_airplane(airplane)

    city = City(1, "Boston", "BOS")
    city_repo.add_city(city)

    return passenger_controller, staff_controller, admin_controller, passenger_repo, staff_repo

# This main function is just to demonstrate the usage
def main():
    passenger_controller, staff_controller, admin_controller, passenger_repo, staff_repo = initialize_data()

    # Get the admin user from the repository
    admin = passenger_repo.get_passenger(3)

    print("\nPassenger Actions:")
    passenger = User(1, "Doe", "John", "123 Main St", "123456789", Role.PASSENGER, "pass123")
    passenger_repo.add_passenger(passenger)
    passenger_controller.book_flight(passenger, 1)
    passenger_controller.view_booking_history(passenger)

    print("\nStaff Actions:")
    staff = User(2, "Smith", "Alice", "456 Birch St", "987654321", Role.STAFF, "staffpass")
    staff_repo.add_staff(staff)
    staff_controller.view_flight_details(staff, 1)
    staff_controller.assign_staff(staff, 1, staff.user_id, "Pilot")

    print("\nAdmin Actions:")
    admin_controller.allocate_aircraft(admin, 1, "1234")
    admin_controller.update_flight_status(admin, 1, "Delayed")
    admin_controller.add_city(admin, City(2, "Chicago", "ORD"))
    admin_controller.remove_city(admin, 1)
    admin_controller.get_all_passengers(admin)

if __name__ == "__main__":
    main()
