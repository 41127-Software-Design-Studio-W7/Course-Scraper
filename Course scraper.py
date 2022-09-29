from bs4 import BeautifulSoup
from bs4 import NavigableString
import re
import json
import os

course_dict = {"subjects": {}}

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r') as f:
            soup = BeautifulSoup(f,'html.parser')

        course_name = str(soup.h1.string)

        course_dict[course_name] = {}
        
        courses_tbody = soup.find_all(True)[0].find_all('table')[2].tbody

        at_course_list = True
        for i, child in enumerate(courses_tbody.children):        
            if isinstance(child, NavigableString):
                continue

            if str(child.string) == "List of majors":
                at_course_list = False
                continue

            if at_course_list == False and child.string == None:
                continue
            else:
                at_course_list = True

            if at_course_list:                
                # This finds the name of the major, the ", Autumn commencing" is not removed
                if (str(child.string).endswith("major")
                    or str(child.string).endswith("commencing")
                    or str(child.string).endswith("full time")):
                        
                    major_name = child.string

                    course_dict[course_name][major_name] = {}
                    #print(child)
                    continue

                # This finds the year of the degree the course is in
                if str(child.string).startswith("Year"):
                    year = child.string
                    course_dict[course_name][major_name][year] = {}
                    continue

                # This finds any "Autumn session" or "Spring session" lines
                try:
                    if str(child.td.em.string).strip().endswith("session"):
                        session = str(child.td.em.string).strip()
                        course_dict[course_name][major_name][year][session] = []
                        continue
                except:
                    pass

                # Anything left at this point contains a course or a "Select X credit points from the following:" statement
                try:
                    #course_dict[course_name][major_name][year][session].
                    course_dict[course_name][major_name][year][session].append(child.td.a.string)

                    credit_points = int(child.find(string=re.compile('\dcp'))[:-2])

                    course_dict["subjects"][child.td.a.string] = {"name": child.td.a.next_sibling.strip(), "credit points": credit_points}
                except:
                    # This except block only occurs when "Select X credit points from the following:" occurs
                    course_dict[course_name][major_name][year][session].append(child.td.string)
                    
                

                    
with open("coursedata.json", "w") as f:
    json.dump(course_dict, f)

