def answer(total_lambs):
    
    # Here's how I solved it..
    
    # From the promblem we know:
    #   MIN Paycheck = sum of previous 2 paychecks
    #   MAX Paycheck = x2 previous paycheck
    
    # I wrote the function "calc_paychecks" that
    # builds lists of paychecks from these rules. 
    
    # ex. total_lambs = 5
    #   min_paychecks = [1, 1, 2]
    #   max_paychecks = [1, 2]

    # The function also handles remaining lambs.
    # When remaining lambs CANNOT pay a FULL paycheck
    # but CAN pay more at least the min_paycheck - 
    # then henchmen is still hired.
    
    # ex. total_lambs = 6
    #   min_paychecks = [1, 1, 2]
    #   max_paychecks = [1, 2, 3] <- 3 is remainder

    def calc_paychecks(total_lambs, max_min):

        # Problem says first paycheck is 1 lamb        
        paychecks = [0,1]
        
        # While there's money left keep hiring henchmen
        while sum(paychecks) < total_lambs:
            # Previous two paychecks
            prev_paycheck_1 = paychecks[-1]
            prev_paycheck_2 = paychecks[-2]
            # Maxmum / Minimum possible paychecks
            max_paycheck = prev_paycheck_1 * 2
            min_paycheck = prev_paycheck_1 + prev_paycheck_2
            
            if max_min == "max":
                paycheck = max_paycheck
            elif max_min == "min":
                paycheck = min_paycheck
    
            remainder = total_lambs - sum(paychecks)
    
            # If remainder can pay FULL salary...
            if remainder >= paycheck:
                paychecks.append(paycheck)
                continue
            # If remainder CANNOT pay FULL salary
            # but CAN pay more than min_paycheck...
            elif remainder >= min_paycheck:
                if max_min == "max":
                    paychecks.append(remainder)
                elif max_min == "min":
                    paychecks.append(min_paycheck)
            # If remainder CANNOT pay more than min_paycheck
            # We're outta lambs, can't afford another paycheck.
            else:
                break
        
        return paychecks

    # Find MAX and MIN number of paychecks
    min_paychecks = calc_paychecks(total_lambs, "min")
    max_paychecks = calc_paychecks(total_lambs, "max")

    # Solution is min-cost-solution minus max-cost-solution!
    solution = len(min_paychecks) - len(max_paychecks)

    return solution
    
