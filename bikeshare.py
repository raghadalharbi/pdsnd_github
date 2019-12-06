import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
      city = input("Which city would you like to search for? New York City, Chicago or Washington?\n")
      if city.title() not in ('New York City', 'Chicago', 'Washington'):
        print("Wrong Input! Please Try again.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month = input("Which month would you like to search for? January, February, March, April, May, June or type 'all'\n")
      if month.title() not in ('January', 'February', 'March', 'April', 'May', 'June','All'):
        print("Wrong Input! Please Try again.")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("Which day would you like to search for? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all'\n")
      if day.title() not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All'):
        print("Wrong Input! Please Try again.")
        continue
      else:
        break

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.lower()])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month.lower() != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day.lower() != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('Calculate The Most Frequent Times of Travel')
    start_time = time.time()

    # TO DO: display the most common month
    print('\nMost Common Month:')
    common_month = df['month'].mode()[0]
    print(common_month)

    # TO DO: display the most common day of week
    print('\nMost Common day:')
    common_day = df['day_of_week'].mode()[0]
    print(common_day)

    # TO DO: display the most common start hour
    print('Most Common Hour:')
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nMost Commonly used start station:')
    common_start_station = df['Start Station'].value_counts().idxmax()
    print(common_start_station)

    # TO DO: display most commonly used end station
    print('\nMost Commonly used end station:')
    common_end_station = df['End Station'].value_counts().idxmax()
    print(common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    print('\nMost Commonly used combination of start station and end station trip:')
    combination = (df['Start Station'] + " - " + df['End Station']).mode()[0]
    print(combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.
    Args:
        data frame
    Returns:
        none
    '''
    head = 0
    tail = 5
    check_input = False
    def display_check(display1):
        if display1.lower() in ['yes','no']:
            return True
        else:
            return False
            print("Wrong Input! Try again.")
    while check_input == False:
        display1 = input('\nWould you like to see more data? '
                        'Type \'yes\' or \'no\'.\n')
        check_input = display_check(display1)
        if check_input == True:
            break
        else:
            print("wrong input. Please type 'yes' or ","'no'")
    if display1.lower() == 'yes':
        print(df[df.columns[0:-1]].iloc[head:tail])
        display2 = ''
        while display2.lower() != 'no':
            check_input2 = False
            while check_input2 == False:
                display2 = input('\nWould you like to see more data? type yes or no \n')
                check_input2 = display_check(display2)
                if check_input2 == True:
                    break
                else:
                    print("wrong input. Please type 'yes' or ","'no'")
            if display2.lower() == 'yes':
                head = head + 5
                tail = tail + 5
                print(df[df.columns[0:-1]].iloc[head:tail])
            elif display2.lower() == 'no':
                break

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\ntotal travel time:')
    ttt = df['Trip Duration'].sum()
    print(ttt)

    # TO DO: display mean travel time
    print('\nmean travel time:')
    mtt = df['Trip Duration'].mean()
    print(mtt)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nCounts of User Types:')
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    print('\nCounts of Gender:')
    try:
      gender = df['Gender'].value_counts()
      print(gender)
    except KeyError:
      print("No available data for Gender.")

    # TO DO: Display earliest, most recent, and most common year of birth
    print('\nEarliest Year of Birth:')
    try:
      earliest_year = df['Birth Year'].min()
      print(earliest_year)
    except KeyError:
      print("No available data for Birth Year.")

    print('\nMost Recent Year:')
    try:
      recent_year = df['Birth Year'].max()
      print(recent_year)
    except KeyError:
      print("No available data for Birth Year.")

    print('\nMost Common Year:')
    try:
      common_year = df['Birth Year'].value_counts().idxmax()
      print(common_year)
    except KeyError:
      print("No available data for Birth Year.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
