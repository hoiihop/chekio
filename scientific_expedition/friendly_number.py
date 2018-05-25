def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    count = 0
    temp = number / base
    while count <= len(powers):
        temp_num = number / base**count
        if count + 1 == len(powers) or -1 < temp < 1:            
            if decimals == 0:
                temp_num = int(temp_num)
            else:
                temp_num = format(temp_num, '.{}f'.format(decimals))
            return '{}{}{}'.format(temp_num, powers[count], suffix)        
        count += 1
        temp /= base


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(friendly_number(255000000000, powers=['', 'k', 'M']))
    #print(friendly_number(-150, base=100, powers=['', 'd', 'D']))
    # assert friendly_number(102) == '102', '102'
    # assert friendly_number(10240) == '10k', '10k'
    # assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    # assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    # assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
