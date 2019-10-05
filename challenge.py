import colors




def challenge_test(inp, testcase):
    try: 
        if(inp==testcase):
            return (colors.fg.green+"SUCCESS "+str(inp) + "="+ str(testcase)+colors.reset)
        else:
            return (colors.fg.red+"Your syntax is correct, but something went wrong. \n\tInput = "+str(inp)+
                    "\n\tInput type = "+str(type(inp))+
                    "\n\tExpected ="+str(testcase)+
                    "\n\tExpected type = "+str(type(testcase))+colors.reset)
    except:
        print(colors.bg.red+"Something went catastrophically wrong, send this to Scott so he can have an interesting day: "+traceback.format_exc())

challenge3 = 2**4*13*19*59
challenge4 = 4613732
challenge5 = 6857
