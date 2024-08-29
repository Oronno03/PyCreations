from datetime import date


def calculate_age(birthday):
    today = date.today()
    if today < birthday:
        return "Invalid birthdate. Please enter a valid date."

    age_year = today.year - birthday.year
    age_month = today.month - birthday.month
    age_day = today.day - birthday.day

    if age_month < 0:
        age_year -= 1
        age_month += 12

    if age_day < 0:
        age_month -= 1
        previous_month = today.month - 1 or 12
        previous_month_year = today.year if previous_month != 12 else today.year - 1
        days_in_previous_month = (
            date(previous_month_year, previous_month + 1, 1)
            - date(previous_month_year, previous_month, 1)
        ).days
        age_day += days_in_previous_month

    return age_year, age_month, age_day


if __name__ == "__main__":
    try:
        birthdate = date(
            year=int(input("Enter year of birth: ")),
            month=int(input("Enter month of birth: ")),
            day=int(input("Enter day of birth: ")),
        )

        year, months, days = calculate_age(birthdate)

        print(f"Age: {year} years, {months} months, {days} days")

    except ValueError:
        print("Invalid input")
