import getpass
import datetime
from main import Role, User, PassengerRepository, StaffRepository, initialize_data, City

def main():
    passenger_controller, staff_controller, admin_controller, passenger_repo, staff_repo = initialize_data()

    print("Welcome to the Airline Management System")
    role = input("Enter your role (Passenger/Staff/Admin): ").strip()

    if role == Role.PASSENGER:
        passenger_id = int(input("Enter your passenger ID: ").strip())
        user = passenger_repo.get_passenger(passenger_id)
        if user:
            print(f"User found: {user.name}, Role: {user.role}")
        else:
            print("User not found in the repository.")
            return

        password = input("Enter your password: ").strip()
        if user and user.password == password and user.role == Role.PASSENGER:
            while True:
                print("\nPassenger Menu")
                print("1. Book Flight")
                print("2. View Booking History")
                print("3. Update Profile")
                print("4. View Details")
                print("5. Exit")
                choice = input("Enter your choice: ").strip()

                if choice == '1':
                    flight_num = int(input("Enter flight number: ").strip())
                    passenger_controller.book_flight(user, flight_num)
                elif choice == '2':
                    passenger_controller.view_booking_history(user)
                elif choice == '3':
                    name = input("Enter new name: ").strip()
                    address = input("Enter new address: ").strip()
                    phone = input("Enter new phone: ").strip()
                    passenger_controller.update_passenger_details(user, name, address, phone)
                elif choice == '4':
                    passenger_controller.view_passenger_details(user)
                elif choice == '5':
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid credentials or role.")

    elif role == Role.STAFF:
        emp_num = int(input("Enter your employee number: ").strip())
        user = staff_repo.get_staff(emp_num)
        if user:
            print(f"User found: {user.name}, Role: {user.role}")
        else:
            print("User not found in the repository.")
            return

        password = input("Enter your password: ").strip()
        if user and user.password == password and user.role == Role.STAFF:
            while True:
                print("\nStaff Menu")
                print("1. View Flight Details")
                print("2. Assign Staff to Flight")
                print("3. Track Certifications")
                print("4. View Employee Details")
                print("5. Exit")
                choice = input("Enter your choice: ").strip()

                if choice == '1':
                    flight_num = int(input("Enter flight number: ").strip())
                    staff_controller.view_flight_details(user, flight_num)
                elif choice == '2':
                    flight_num = int(input("Enter flight number: ").strip())
                    emp_num = int(input("Enter staff ID to assign: ").strip())
                    role = input("Enter role for the staff: ").strip()
                    staff_controller.assign_staff(user, flight_num, emp_num, role)
                elif choice == '3':
                    emp_num = int(input("Enter staff ID to track certifications: ").strip())
                    staff_controller.track_certifications(user, emp_num)
                elif choice == '4':
                    emp_num = int(input("Enter employee ID to view details: ").strip())
                    staff_controller.view_employee_details(user, emp_num)
                elif choice == '5':
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid credentials or role.")

    elif role == Role.ADMIN:
        print("Contents of passenger_repo:")
        for user in passenger_repo.passengers:
            print(f"User ID: {user.user_id}, Name: {user.name}, Role: {user.role}")

        user_id = int(input("Enter your ID: ").strip())
        user = passenger_repo.get_passenger(user_id)
        if user:
            print(f"User found: {user.name}, Role: {user.role}")

            password = input("Enter your password: ").strip()
        else:
            print("User not found in the repository.")
            return

        if user and user.password == password and user.role == Role.ADMIN:
            while True:
                print("\nAdmin Menu")
                print("1. Allocate Aircraft")
                print("2. Update Flight Status")
                print("3. Add City")
                print("4. Remove City")
                print("5. View All Passengers")
                print("6. Hire Employee")
                print("7. Update Employee")
                print("8. Manage Flight Route")
                print("9. Schedule Flight")
                print("10. Cancel Flight")
                print("11. Add Airplane")
                print("12. Update Airplane")
                print("13. Decommission Airplane")
                print("14. View Airplane Details")
                print("15. View City Details")
                print("16. Exit")
                choice = input("Enter your choice: ").strip()

                if choice == '1':
                    flight_num = int(input("Enter flight number: ").strip())
                    serial_num = input("Enter aircraft serial number: ").strip()
                    admin_controller.allocate_aircraft(user, flight_num, serial_num)
                elif choice == '2':
                    flight_num = int(input("Enter flight number: ").strip())
                    new_status = input("Enter new flight status: ").strip()
                    admin_controller.update_flight_status(user, flight_num, new_status)
                elif choice == '3':
                    city_id = int(input("Enter city ID: ").strip())
                    name = input("Enter city name: ").strip()
                    airport = input("Enter airport code: ").strip()
                    admin_controller.add_city(user, City(city_id, name, airport))
                elif choice == '4':
                    city_id = int(input("Enter city ID to remove: ").strip())
                    admin_controller.remove_city(user, city_id)
                elif choice == '5':
                    admin_controller.get_all_passengers(user)
                elif choice == '6':
                    emp_num = int(input("Enter employee number: ").strip())
                    surname = input("Enter surname: ").strip()
                    name = input("Enter name: ").strip()
                    address = input("Enter address: ").strip()
                    phone = input("Enter phone: ").strip()
                    salary = float(input("Enter salary: ").strip())
                    role = input("Enter role: ").strip()
                    type_rating = input("Enter type rating: ").strip()
                    admin_controller.hire_employee(user, emp_num, surname, name, address, phone, salary, role, type_rating)
                elif choice == '7':
                    emp_num = int(input("Enter employee number: ").strip())
                    name = input("Enter new name (leave blank to keep current): ").strip()
                    address = input("Enter new address (leave blank to keep current): ").strip()
                    phone = input("Enter new phone (leave blank to keep current): ").strip()
                    salary = input("Enter new salary (leave blank to keep current): ").strip()
                    type_rating = input("Enter new type rating (leave blank to keep current): ").strip()
                    admin_controller.update_employee(user, emp_num, name if name else None, address if address else None, phone if phone else None, float(salary) if salary else None, type_rating if type_rating else None)
                elif choice == '8':
                    flight_num = int(input("Enter flight number: ").strip())
                    origin = input("Enter new origin: ").strip()
                    dest = input("Enter new destination: ").strip()
                    intermediate_cities = input("Enter intermediate cities (comma separated): ").strip().split(',')
                    admin_controller.manage_flight_route(user, flight_num, origin, dest, intermediate_cities if intermediate_cities[0] else None)
                elif choice == '9':
                    flight_num = int(input("Enter flight number: ").strip())
                    date = input("Enter new date (YYYY-MM-DD): ").strip()
                    arr_time = input("Enter new arrival time (HH:MM): ").strip()
                    dep_time = input("Enter new departure time (HH:MM): ").strip()
                    admin_controller.schedule_flight(user, flight_num, datetime.datetime.strptime(date, '%Y-%m-%d').date(), arr_time, dep_time)
                elif choice == '10':
                    flight_num = int(input("Enter flight number to cancel: ").strip())
                    admin_controller.cancel_flight(user, flight_num)
                elif choice == '11':
                    serial_num = input("Enter aircraft serial number: ").strip()
                    manufacturer = input("Enter manufacturer: ").strip()
                    model = input("Enter model: ").strip()
                    admin_controller.add_airplane(user, serial_num, manufacturer, model)
                elif choice == '12':
                    serial_num = input("Enter aircraft serial number: ").strip()
                    manufacturer = input("Enter new manufacturer (leave blank to keep current): ").strip()
                    model = input("Enter new model (leave blank to keep current): ").strip()
                    admin_controller.update_airplane(user, serial_num, manufacturer if manufacturer else None, model if model else None)
                elif choice == '13':
                    serial_num = int(input("Enter aircraft serial number to decommission: ").strip())
                    admin_controller.decommission_airplane(user, serial_num)
                elif choice == '14':
                    serial_num = int(input("Enter aircraft serial number: ").strip())
                    admin_controller.view_airplane_details(user, serial_num)
                elif choice == '15':
                    city_id = int(input("Enter city ID: ").strip())
                    admin_controller.view_city_details(user, city_id)
                elif choice == '16':
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid credentials or role.")
    else:
        print("Invalid role.")

if __name__ == "__main__":
    main()
