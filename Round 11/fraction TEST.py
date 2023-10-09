factor = greatest_common_divisor(self.__numerator, self.__denominator)
        return (self.__numerator//factor, self.__denominator//factor)
