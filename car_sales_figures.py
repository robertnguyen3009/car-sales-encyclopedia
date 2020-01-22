# Robert Nguyen

from easygui import *

#-------------------------------------------------------------------------------

class Car:
    '''
    Fields: _brand is a string containing the storm name
            _model is a string containing the date the storm formed in MMDD
            _sales is a non-negative integer containing the sales
    '''
    
    def __init__(self, brand, model, sales):
        self._brand = brand
        self._model = model
        self._sales = int(sales)
    
    ## print(self) prints Car
    def __str__(self):
        return 'Car({0}, {1}, {2})'.format(self._brand, self._model, \
                                           self._sales)
    
    ## self.brand() returns the brand name
    def brand(self):
        return self._brand
    
    ## self.model() returns the model name
    def model(self):
        return self._model
    
    ## self.sales() returns the number units sold
    def sales(self):
        return self._sales
    
    ## self == other produces True if self and other have the same
    ##     size and store the same sales amounts at each index.
    ## __eq__: Car Car -> Bool
    def __eq__(self, other):
        if self.sales() == other.sales():
            return True
        
        else:
            return False
    
    ## self.car_name() returns name of the car
    def car_name(self):
        return '{0} {1}'.format(self.brand(), self.model())
    
    ## self.car_name() returns name of the car
    def sentence(self):
        abc = str(self.sales())
        figure = ''
        
        for bac in range (1, len(abc) + 1):
            figure = abc[-bac] + figure
            if bac%3 == 0 and len(abc) - bac != 0:
                figure = ',' + figure

        if self.sales() == 1:
            return '{0} {1} sold {2} unit'.format(self.brand(), \
                                                  self.model(), \
                                                  figure)
        
        else:
            return '{0} {1} sold {2} units'.format(self.brand(), \
                                                   self.model(), \
                                                   figure)

#-------------------------------------------------------------------------------

salesfile = open('cars2019.txt', 'r')

brand_names = []
car_list = []
first_line = salesfile.readline()
first_line.strip()

while first_line != '':
    first_line = salesfile.readline()
    first_line.strip()
    
    if first_line != '' and first_line[0:4] != 'Make':
        c = first_line.split(',')
        car = Car(c[0], c[1], c[2])
        if car.brand() not in brand_names:
            brand_names.append(car.brand())
        
        car_list.append(car)
    
ss = True

while ss == True:
    c1 = ['View Brand', 'View Model', 'Compare Two Models', 'Quit']
    opt1 = buttonbox('What would you like to do?', 'Main Menu', c1, None, \
                     None, None, 'Quit')
    if opt1 == 'Quit':
        ss = False
        break
    
    opt2 = choicebox('Select a Brand.', 'Brands', brand_names)
    
    model_list = car_list[:]
    model_name_list = []
    for x in car_list:
        if x.brand() != opt2:
            model_list.remove(x)
        else:
            model_name_list.append(x.model())
    
    if opt2 == None:
        ss = False
        break
    
    if opt1 == c1[0]:
        sales_list = []
        for y in model_list:
            sales_list.append(y.sales())
        sales_count = sum(sales_list)
        model_count = len(sales_list)
        sales_average =  int(sales_count/model_count)
        best_seller = max(sales_list)
        bs_index = sales_list.index(best_seller)
        figures = []
        
        for z in [sales_count, sales_average]:
            a = str(z)
            figure = ''
            
            for b in range (1, len(a) + 1):
                figure = a[-b] + figure
                if b%3 == 0 and len(a) - b != 0:
                    figure = ',' + figure
                
                elif len(a) - b == 0:
                    figures.append(figure)
        
        x1 = 'Total Sales: {0}\nModels: {1}\nAverage Sales per Model: {2}\n'\
            .format(figures[0], model_count, figures[1])
        x2 = 'Best Seller: {0}'.format(model_list[bs_index].sentence())
        
        msg1 = msgbox('{0}{1}'.format(x1,x2), 'Brand Summary', 'OK')
    else:
        cm1 = choicebox('Select a Model.', 'Models', model_name_list)
        
        if cm1 == None:
            ss = False
            break
        
        for f in model_list:
            if f.model() == cm1:
                g1 = f
        
        if opt1 == c1[1]:
            msg2 = msgbox(g1.sentence(), 'Model Summary', 'OK')
        
        elif opt1 == c1[2]:
            opt2a = choicebox('Select Another Brand.', 'Brands', brand_names)
            model_list_2 = car_list[:]
            model_name_list_2 = []
            
            for d in car_list:
                if d.brand() != opt2a:
                    model_list_2.remove(d)
                else:
                    model_name_list_2.append(d.model())
            
            cm2 = choicebox('Select Another Model.', 'Models', \
                            model_name_list_2)
            
            if cm2 == None:
                ss = False
                break
            
            for h in model_list_2:
                if h.model() == cm2:
                    g2 = h
            
            if g1.sales() >= g2.sales():
                g = g1
                j = g2
            
            else:
                g = g2
                j = g1
            
            g_j = g.sales() - j.sales()
            gif = str(self.sales())
            figureplus = ''
            
            for fig in range (1, len(gif) + 1):
                figure = gif[-fig] + figure
                if fig%3 == 0 and len(gif) - fig != 0:
                    figureplus = ',' + figureplus
            
            if g_j == 0:
                x1 = 'The {0} and the {1} sold the same amount.'.format(\
                    g.car_name(), j.car_name())
            
            elif g_j == 1:
                x1 = 'The {0} sold 1 more units than the {2}.'.format(\
                    g.car_name(), j.car_name())
            
            else:
                x1 = 'The {0} sold {1} more units than the {2}.'.format(\
                    g.car_name(), figureplus, j.car_name())
            
            msg3 = msgbox('The {0} \nwhile {1}.\n{2}'.format(g.sentence(), \
                                                             j.sentence(), x1))
    

    if ss == False:
        break    