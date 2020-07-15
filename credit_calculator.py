import math
import sys
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str)
parser.add_argument("--principal", type=int)
parser.add_argument("--payment", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args()

if args.type not in ("diff", "annuity") or args.type == "diff" and args.payment is not None or args.interest is None:
    print("Incorrect parameters.")
elif args.periods is None: 
    if args.principal <= 0 or args.payment <= 0 or args.interest <= 0:
        print("Incorrect parameters.")
    else:
        months = math.ceil(math.log(args.payment / (args.payment - (args.interest / 1200) * args.principal), 1 + (args.interest / 1200)))
        overpayment = abs(math.ceil(args.payment) * months - args.principal)
        if months < 12:
            if months == 1:
                print('You need 1 month to repay this credit!')
            else:
                print(f'You need {months} months to repay this credit!')
        else:
            years = months // 12
            months = months % 12
            if years == 1:
                if months == 0:
                    print('You need 1 year to repay this credit!')
                elif months == 1:
                    print('You need 1 year and 1 month to repay this credit!')
                else:
                    print(f'You need 1 year and {months} months to repay this credit!')
            else:
                if months == 0:
                    print(f'You need {years} years to repay this credit!')
                elif months == 1:
                    print(f'You need {years} years and 1 month to repay this credit!')
                else:
                    print(f'You need {years} years and {months} months to repay this credit!')
        print(f'Overpayment = {overpayment}')
elif args.principal is None:
    if args.periods <= 0 or args.payment <= 0 or args.interest <= 0:
        print("Incorrect parameters.")
    else:
        principal = args.payment / (args.interest / 1200 * math.pow(args.interest / 1200 + 1, args.periods) / (math.pow(1 + args.interest / 1200, args.periods) - 1))
        overpayment = args.payment * args.periods - principal
        print(f'''Your credit principal = {principal}!
        Overpayment = {overpayment}''')
elif args.payment is None:
    if args.periods <= 0 or args.principal <= 0 or args.interest <= 0:
        print("Incorrect parameters.")
    elif len(sys.argv) < 5:
        print("Incorrect parameters.")
    elif args.type == "annuity":
        payment = math.ceil(args.principal * ((args.interest / 1200) * math.pow(args.interest / 1200 + 1, args.periods) / (math.pow(1 + args.interest / 1200, args.periods) - 1)))
        overpayment = payment * args.periods - args.principal
        print(f'''Your annuity payment = {payment}!
        Overpayment = {overpayment}''')
    elif args.type == "diff":
        current_month = 0
        total_paid = 0
        for i in range (args.periods):
            current_month +=1
            pay = math.ceil(args.principal / args.periods + args.interest / 1200 * (args.principal - (args.principal * (current_month - 1) / args.periods)))
            total_paid += pay
            print(f"Month {current_month}: paid out {pay}")
        overpayment = total_paid - args.principal
        print(f'Overpayment = {overpayment}')
    
    
