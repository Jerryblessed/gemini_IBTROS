import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyA4ByLRJXvKVXlZdnT_9bRaaX1RAaq04DQ")


l = "Destination-route:Dawko MFM(Dwako, Abuja, Nigeria) JRJ Excellet academy(Aldenco Abuja, Nigeria) Time-frame: 8:00AM - 6:PM User Name: Mr. David Ope username: @david bright" 
m = "Destination-route: Library, senate-building Time-frame: 8:00AM - 6:PM User Name: Mr. David Ope User Number: 09044559334"
# model = genai.GenerativeModel('gemini-1.5-flash')
# response = model.generate_content(f"write the most common complete group from these {l, m}, from the question only (no explanations just raw answers), I want to go to a place to read ")
# print(response.text)

print(f"write the most common complete group from these {l, m}, from the question only (no explanations just raw answers), I want to go to a place to read ")