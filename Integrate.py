
import numpy as np
class Integrate:
    
# approximates integral using rectangle method
    def rectint(f,a,b,rectangles):
        cumulative_area=0

        a=float(a)
        b=float(b)
        rectangles=float(rectangles)

        i=(b-a)/rectangles

        trailing_x=a
        leading_x=a+i

        while (a<=leading_x<=b) or (a>=leading_x>=b):
            area=f((trailing_x+leading_x)/2)*i
            cumulative_area+=area

            leading_x+=i
            trailing_x+=i

        return cumulative_area
# approximates integral using trapizoid method
    def trapint(f,a,b,trapezoids):
        cumulative_area=0

        a=float(a)
        b=float(b)
        trapezoids=float(trapezoids)

        i=(b-a)/trapezoids

        trailing_x=a
        leading_x=a+i

        while (a<=leading_x<=b) or (a>=leading_x>=b):
            area=(f(trailing_x)+f(leading_x))*i/2
            cumulative_area+=area

        leading_x+=i
        trailing_x+=i

        return cumulative_area
      
 # approximates the integral using gauss-legendre quadrature 
    def GaussLeg(f, a, b):
        a=float(a)
        b=float(b)
        #Evaluation points for the gaussian quadrature
        X=[-0.90618,-0.538469,0,0.538469,0.90618]
        #Weights for the gaussian quadrature
        W=[0.236927,0.478629,0.568889,0.478629,0.236927]

        #Converting my x values to change integrand from [-1,1] to [a,b]
        x=[]
        for i in range(len(X)):
            x.append((b+a)/2 + (b-a)/2 *X[i])
        
        #calculating the area of each rectangle using quadrature
        area=[]
        for i in range(len(X)):
            area.append(((b-a)/2)*W[i]*f(x[i]))

        #summing up all the areas
        cumulative_area=sum(area)

        return cumulative_area