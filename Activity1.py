def check_exam_eligibility(age):
  
    if age >= 18:
        return True
    else:
        return False

def main():
 
    try:
        age = int(input("Enter your current age: "))
        
        if check_exam_eligibility(age):
            print("You are eligible to take the exam.")
        else:
            print("You are not eligible to take the exam.")
    
    except ValueError:
        print("Invalid input. Please enter a valid age.")

if __name__ == "__main__":
    main()