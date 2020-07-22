import sys
import datetime
import constant as con
from urllib.request import urlopen as u_req
from bs4 import BeautifulSoup as soup

## @class       fromWeb
#  @brief       Load and sort data from a web page to a dict.
#  @author      Michael Semekla
#  @date        19.07.2020
#  @version     0.1
#  @details     Load data from web page, select relevant information
#               and safe them to an dict.
   

class fromWeb:

    __page_lecture_period : str ## @var string __page_lecture_period_url Hold web page from lecture period time url
    __page_exam_period : str    ## @var string __page_exam_period_url Hold web page from exam period url

    __container_lecture_period : [str] ## @var string_array __container_lecture_period Hold separated information from web pag url.
    __container_exam_period :[str] ## @var string_array __container_exam_period Hold separated information from web pag url.

    ## @var dict __information_from_web Hold sorted information from both container. 
    __information_from_web = {
        'semester_name' : [str],
        'semester_period_begin' : [datetime],
        'semester_period_end' : [datetime],
        'semester_break_begin' : [datetime],
        'semester_break_end' : [datetime],
        'exam_phase_1_begin' : [datetime],
        'exam_phase_1_end' : [datetime],
        'exam_phase_2_begin' : [datetime],
        'exam-phase_2_end' :[datetime],
        'registration_period_phase_1_begin' : [datetime],
        'registration_period_phase_1_end' : [datetime],
        'registration_period_phase_2_begin' : [datetime],
        'registration_period_phase_2_end' : [datetime]
    }

    ## @fn          __init__()
    #  @brief       Constructor from fromWeb
    #
    #  @param       object self The object of fromWeb.
    #  @return      -
    #        
    #  @details     Initiate the object of the class fromWeb.

    def __init__(self):
        self.__load_data_from_web()
        pass
        
    ## @fn          load_data_from_web()
    #  @brief       Load html page from url.
    #
    #  @param       object self The object of fromWeb.
    #  @return      -
    #        
    #  @details     Load html page from url, stored in self.__lecture_period_url 
    #               and self.__exam_period_url.Safe the page as string in 
    #               self.__page_lecture_period and self.__page_exam_period.
         
    def __load_data_from_web(self):

        try:
            u_client_1 = u_req(con.LECTURE_PERIOD_URL)
            self.__page_lecture_period_url = u_client_1.read()
            u_client_1.close()
        except:
            e = sys.exc_info()[0]
            print( "<p>Error: %s</p>" % e )
        
        try:
            u_client_2 = u_req(con.EXAM_PERIOD_URL)
            self.__page_exam_period_url = u_client_1.read()
            u_client_2.close()
        except:
            e = sys.exc_info()[0]
            print( "<p>Error: %s</p>" % e )


    ## @fn          get_information_from_web()      
    #  @brief       Getter function.
    #  
    #  @param       object self The object of fromWeb.
    #  @return      dict __information_from_web The dict from class fromWeb
    #
    #  @details     Get self.__information_from_web from class fromWeb.

    def get_information_from_web(self):
        return self.__information_from_web


