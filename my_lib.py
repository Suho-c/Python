# 함수 이름 : my_unique() 함수
# 함수 설명 : list 형식의 데이터를 인수로 전달 받아 고유값 list를 반환하는 함수
# 인수 : 고유값을 얻고자 하는 데이터를 가지고 있는 list
# 반환값 : 고유값을 가지고 있는 list
def my_unique( arg ):
    result = []
    full = False # flag 변수
    
    for value in arg:
        if not full and len( result ) == 0:
            result.append( value )
            full = True
        
        count = result.count( value )        
        if count == 0:
            result.append( value )

    result = sorted( result )    

    return result

# 함수 이름 : average_standard_deviation()
# 함수 설명 : 평균과 표준편차를 반환하는 함수
# 인수 : 평균과 표준편차를 구하고자 하는 list
# 반환값 : 평균과 분산, 표준편차 tuple
def average_standard_deviation( arg ):
    average = sum( arg ) / len( arg )
    
    deviation = []
    for value in arg:
        deviation.append( value - average )
        
    deviation_square = []
    for value in deviation:
        deviation_square.append( value * value )
        
    dispersion = sum( deviation_square ) / len( deviation_square )
    
    
    standard_deviation = dispersion ** ( 1 / 2 )
    
    return ( average, dispersion, standard_deviation )

# 함수 이름 : calculate_quartile()
# 함수 설명 : 1사분위수, 2사분위수, 3사분위수를 반환하는 함수
# 인수 : 사분위수를 구하고자 하는 list
# 반환값 : 1사분위수, 2사분위수, 3사분위수 tuple
def calculate_quartile( arg ):
    sort_list = sorted( arg )
    
    # ( ( 총도수 - 1 ) X 0.25 ) + 1 : 1사분위수( 하위 25% )
    location_25 = int( ( ( len( sort_list ) - 1 ) * 0.25 ) + 1 )
    
    # ( ( 총도수 - 1 ) X 0.50 ) + 1 : 2사분위수( 하위 50% )
    location_50 = int( ( ( len( sort_list ) - 1 ) * 0.50 ) + 1 )
    
    # ( ( 총도수 - 1 ) X 0.75 ) + 1 : 3사분위수( 하위 75% )
    location_75 = int( ( ( len( sort_list ) - 1 ) * 0.75 ) + 1 )
    
    return ( sort_list[ location_25 ], sort_list[ location_50 ],
             sort_list[ location_75 ] )

# 함수 이름 : my_mean()
# 함수 설명 : 평균 계산 함수
# 인수 : 평균을 구할 대상 list
# 반환값 : 평균
def my_mean( arg ):
    result = 0
    len_arg = len( arg )
    for v in arg:
        result += v
    result = result / len_arg 

    return result

# 함수 이름 : my_sqrt()
# 함수 설명 : 제곱근 계산 함수
# 인수 : 제곱근을 구할 대상 list
# 반환값 : 제곱근
def my_sqrt( arg ):
    result = arg / 2
    for i in range( 30 ): # 반복 횟수 증가에 따라 정확도 상승
        result = ( result + ( arg / result ) ) / 2

    return result

# 함수 이름 : my_corr()
# 함수 설명 : 피어슨 상관 계수 계산 함수
# 인수 : 피어슨 상관 계수를 계산할 대상 변수
# 반환값 : 피어슨 상관 계수 
def my_corr( arg1, arg2 ):
    # 평균 계산
    mean_arg1 = my_mean( arg1 )
    mean_arg2 = my_mean( arg2 )

    # 분자
    numerator = 0
    for i in range( len( arg1 ) ):
        numerator += ( arg1[ i ] - mean_arg1 ) * ( arg2[ i ] - mean_arg2 )

    # 분모
    x_denominator = 0
    for i in range( len( arg1 ) ):
        x_denominator += ( arg1[ i ] - mean_arg1 ) ** 2
    
    y_denominator = 0
    for i in range( len( arg2 ) ):
        y_denominator += ( arg2[ i ] - mean_arg2 ) ** 2
    
    denominator = my_sqrt( x_denominator ) * my_sqrt( y_denominator )
    result = numerator / denominator

    return result


#
# 클래스명 : Stack
#          고정 길이 stack
#
# stack 생성 : Stack( 용량 )
# data push : stack_push( 값 ) - True/False 성공 유무 반환
# data pop : stack_pop() - 데이터 반환, None : stack에 데이터 없는 경우 반환
# 상태 확인
#         get_top() : 현재 top 위치
#         get_length() : 현재 stack에 저장된 데이터 개수
#
class Stack:
    def __init__( self, capacity ):
        self.__capacity = capacity # stack 용량
        self.__length = 0 # stack 길이( 데이터 개수 )
        self.__top = -1 # top 위치
        self.__stack = [] # stack 저장 공간
        
    def stack_push( self, data ):
        result = False
        
        if not self.__isoverflow():
            self.__stack.append( data )
            self.__length += 1
            self.__top += 1
            result = True
            
        return result
            
    def stack_pop( self ):
        result = None
        
        if not self.__isunderflow():
            result = self.__stack[ self.__top ]
            del self.__stack[ self.__top ]
            self.__length -= 1
            self.__top -= 1
            
        return result
    
    def get_top( self ):
        return self.__top
    
    def get_length( self ):
        return self.__length
    
    def __isoverflow( self ): 
        result = False
        
        if self.__length == self.__capacity:
            result = True
        
        return result
    
    def __isunderflow( self ):
        result = False
        
        if self.__length == 0:
            result = True
            
        return result
    
    def __str__( self ):
        return self.__repr__()
    
    def __repr__( self ):
        result = ''
        
        for v in self.__stack:
            result += f'{v:3}'
        
        return result

# 이상치 기준값 제공 함수
#
# 이상치는 중앙값을 크게 벗어난 값( 중앙값 기준 1.5배 넘어가는 값 )
# IQR : 1사분위수와 3사분위수의 차이값
#
# 1사분위수 - ( 1.5 )IQR
# 3사분위수 + ( 1.5 )IQR
def outlier_criteria( x, column ):
    # Q1( 1사분위수 ), Q2( 2사분위수 ) 구하기
    q1 = x[ column ].quantile( 0.25 )
    q3 = x[ column ].quantile( 0.75 )
    
    # 이상치 : 1.5 * IQR( Q3 - Q1 )
    iqr = 1.5 * ( q3 - q1 )
        
    iqr1 = q1 - iqr
    iqr3 = q3 + iqr
    
    return ( iqr1, iqr3 )

# 이상치 대체값 설정 함수
def change_outlier( data, column ):
    x = data.copy()
    
    # 이상치 기준값 계산
    iqr1, iqr3 = outlier_criteria( x, column )
    
    # 이상치 대체값 설정( 최소값, 최대값)
    standard_min = 0
    if iqr1 > 0:
        change_min = iqr1
    standard_max = iqr3
    
    # 이상치 대체
    x.loc[ ( x[ column ] > standard_max ), column ] = standard_max
    x.loc[ ( x[ column ] < standard_min ), column ] = standard_min
    
    return x
    

def print_outlier( x, column ):
    # 이상치 기준값 계산
    iqr1, iqr3 = outlier_criteria( x, column )
    
    print( f'이상치 기준값 : {round( iqr1, 3 )}, {round( iqr3, 3 )}\n' )
    outlier = list ( x[ ( x[ column ] > iqr3 ) | ( x[ column ] < iqr1 ) ][ column ] )
    
    print( f'{column} 변수 이상치\n' )
    print( outlier )
    print( f'\n{column} 변수 이상치 개수 : {len( outlier )}개' )