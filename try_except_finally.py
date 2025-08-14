try:
    age_data = input('Enter the age')
    age_data_new = age_data + 10
    raise TypeError('value error')
    print(age_data)
except TypeError as e:
    print(f'Error in data as {e}')
except ZeroDivisionError as e:
    print(f'Error in data as {e}')
finally:                                            #finally - always works
    print('Calculations are completed')