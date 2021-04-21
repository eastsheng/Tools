'''temperature profile average'''
import numpy as np
import matplotlib.pyplot as plt
# np.set_printoptions(suppress=True)
# np.set_printoptions(threshold=100000000)

def temperature(t_file,loop,layer_number,fixed_layer_number,length_system,fit_factor=5):
  temp=[]
  try:
    for i in range(loop):
      t = np.loadtxt(t_file,dtype=float,skiprows=(layer_number+1)*i+4,
                    max_rows=layer_number,usecols=(3))
      temp.append(t)
  except StopIteration:
    print('Here is stop',i)
  # print(t.shape)
  # print(temp)
  temp = np.array(temp)
  # print(temp.shape)
  # print(temp)
  mean_value = np.mean(temp,axis=0)
  # print(mean_value)

  lf = layer_number-fixed_layer_number
  lff = layer_number-2*fixed_layer_number
  x = np.linspace(fixed_layer_number,lf,lff)

  x = x/layer_number*length_system #nm
  mean_value = mean_value[fixed_layer_number:lf]

  x2 = x[fit_factor:layer_number-fit_factor]
  y2 = mean_value[fit_factor:layer_number-fit_factor]

  fit = np.polyfit(x2,y2,1)
  fit_fn = np.poly1d(fit)
  print("斜率-温度梯度:" ,fit[0],"(K/nm)","\n"+"截距:",fit[1],"(K)")
  plt.scatter(x,mean_value)
  plt.plot(x2,fit_fn(x2),"r-",linewidth=4.0)
  plt.text(5, 320, str(fit[0]),fontsize=25)

  plt.show()

  DeltaT = fit[0]*(length_system-2*fixed_layer_number*(length_system/layer_number))
  print('DeltaT=',DeltaT)


  return


# --------main program--------#

if __name__ == '__main__':
  t_file  ='./1_CNTtemp.profile'
  tot_step = 2000000
  interval_step = 10000
  loop = int(tot_step/interval_step)
  layer_number = 100
  fixed_layer_number = 4
  length_system = 45.42350494461803
  fit_factor = 21
  temperature(t_file,loop,layer_number,fixed_layer_number,length_system,fit_factor=fit_factor)
  # print(4.5084876661858857e+02--3.3862828275917187e+00)