#This program calculates the final score

#Preliminary design report out of 100 points
def preliminary_designscoring():
  print("Preliminary Design scores")
  design_trade_studies = int(input("Enter the design trade studies score out of 15 points: "))
  technical_innovations = int(input("Enter the technical innovations score out of 15 points: "))
  prelim_CAD_models = int(input("Enter the preliminatry CAD models score out of 30 points: "))
  fabrication_methods = int(input("Enter the fabrication methods score out of 15 points: "))
  gaant_chart = int(input("Enter the gaant chart score out of 5 points: "))
  report_clarity = int(input("Enter the report clarity score out of 20 points: "))
  total_prelim_score = design_trade_studies+technical_innovations+prelim_CAD_models+fabrication_methods+gaant_chart+report_clarity
  return total_prelim_score
#Final technical report score out of 100 points
def final_technical_report():
  print("Final Design Scores")
  design_trade_studies = int(input("Enter the design trade studies score out of 5 points: "))
  technical_innovations = int(input("Enter the technical innovations score out of 15 points: "))
  final_CAD_models = int(input("Enter the final CAD models score out of 30 points: "))
  fabrication_methods = int(input("Enter the fabrication methods score out of 15 points: "))
  flight_test = int(input("Enter the flight test results score out of 15 points: "))
  report_clarity = int(input("Enter the report clarity score out of 20 points: "))
  total_final_tech_score = design_trade_studies+technical_innovations+final_CAD_models+fabrication_methods+flight_test+report_clarity
  return total_final_tech_score
#The total presentation score
def presentation_score():
  print("Presentation Scores")
  originality = int(input("Enter the originality score out of 15 points: "))
  presentation = int(input("Enter the presentation score out of 15 points: "))
  engineering = int(input("Enter the engineering score out of 30 points: "))
  publicity = int(input("Enter the publicity score out of 15 points: "))
  teamwork = int(input("Enter the flight test results score out of 15 points: "))
  public_relations = int(input("Enter the report clarity score out of 20 points: "))
  total_presenation_score = originality+presentation+engineering+publicity+teamwork+public_relations
  return total_presenation_score

#The total maneuverability score is 150 possible points
def maneuverability_course_scoring(N):
  n = int(input("Enter nth place where 1 is the fastest team: "))
  fastest_time_score = 150*((N+2)-n)/(N+1)
  return fastest_time_score

#The total maximum range course lap scoring is 100 possible points
def max_range_course_lap_scoring(N):
  n = int(input("Enter nth place where 1 is the team with the most laps: "))
  maximum_range_course_score = 100*((N+2)-n)/(N+1)
  return maximum_range_course_score
#The total maximum payload fraction scoring is 50
def payload_fraction_scoring(N):
  payload_weight = int(input("Enter payload weight:"))
  aircraft_wo_payload = int(input("Enter aircraft weight without payload: "))
  payload_fraction = payload_weight/aircraft_wo_payload
  n = int(input("Enter nth place where 1 is the highest payload fraction: "))
  maximum_payload_fraction_scoring = 50*((N+2)-n)/(N+1)
  return payload_fraction, maximum_payload_fraction_scoring 
# 25 points are awarded for successful completion of the bonus
def bonus_scoring():
  bonus = input("Successfully complete bonus? (Y or N)")
  if bonus == 'Y' or bonus == 'y':
    return 25
  else:
    return 0
#This allows to write into a txt file to compile and compare results
def write_into_txt(total_score,maneuverability_scoring,max_range_lap_scoring,payload_fract_scoring,bonus_score,total_range,payload_fract):
  compile = input("Would you like to export these scores into a txt file to save them? (Y or N)")
  if compile == 'Y' or compile =='y':
    total_score = str(total_score)
    maneuverability_scoring = str(maneuverability_scoring)
    max_range_lap_scoring = str(max_range_lap_scoring)
    payload_fract_scoring = str(payload_fract_scoring)
    bonus_score = str(bonus_score)
    total_range = str(total_range)
    payload_fract = str(payload_fract)
    Scorescompiled = open("Scorescompiled.txt","w")
    Scorescompiled.write(f"The total calculated score is " + total_score +"\n")
    Scorescompiled.write(f"The maneuverability score is " + maneuverability_scoring+"\n")
    Scorescompiled.write(f"The total range score is " + total_range+"\n")
    Scorescompiled.write(f"The range course lap score is " + max_range_lap_scoring +"\n")
    Scorescompiled.write(f"The payload fraction is " + payload_fract +"\n")
    Scorescompiled.write(f"The payload fraction score is " + payload_fract_scoring +"\n")

def run():
  N = int(input("Enter the number of teams: "))
  preliminary_design_score = preliminary_designscoring()
  final_technical_report_score = final_technical_report()
  presentation_scoring = presentation_score()
  maneuverability_scoring = maneuverability_course_scoring(N)
  max_range_lap_scoring = max_range_course_lap_scoring(N)
  payload_fract, payload_fract_scoring = payload_fraction_scoring(N)
  bonus_score = bonus_scoring()
  total_score = preliminary_design_score + presentation_scoring+ final_technical_report_score + maneuverability_scoring + max_range_lap_scoring + payload_fract_scoring + bonus_score
  print(f"The total calculated score is {total_score}")
  print(f"The maneuverability score is {maneuverability_scoring}")
  total_range = max_range_lap_scoring + payload_fract_scoring
  print(f"The total range score is {total_range}")
  print(f"The range course lap score is {max_range_lap_scoring}")
  print(f"The payload fraction score is {payload_fract_scoring}")
  print(f"The payload fraction is {payload_fract}")
  write_into_txt(total_score,maneuverability_scoring,max_range_lap_scoring,payload_fract_scoring,bonus_score,total_range,payload_fract)

if __name__ == "__main__":
  run()
