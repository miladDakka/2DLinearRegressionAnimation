#!/usr/bin/env python
# coding: utf-8
import matplotlib.pyplot as plt
import tensorflow, torch
from matplotlib import animation, rc
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
rc('animation', html='html5')

plt.rcParams['animation.ffmpeg_path'] = 'C:\\ProgramData\\Anaconda3\\pkgs\\ffmpeg-4.2-h6538335_0\\Library\\bin\\ffmpeg.exe'
writer = animation.FFMpegWriter()

def mse(y_hat,y): return ((y_hat-y)**2).mean()

def update():
    #find all predicted y values
    y_hat = x@a
    #calculate MSE loss
    loss = mse(y,y_hat)
    #calculate the gradient, where variable 
    #'grad' now contains gradient value
    loss.backward()
    #we turn the gradient calculation off
    #while doing the SGD update
    with torch.no_grad():
        #substitute from a (and replace with) 
        #the value of lr*a.grad
        a.sub_(lr * a.grad)
        #set the gradient to zero since the
        #backward() function accumulates loss
        a.grad.zero_()

n=50
x = torch.ones(n,3);
x[:,0].uniform_(-1.,1);
x[:,1].uniform_(-1.,1);
a = torch.tensor([-7.,-7,0])
y=x@a+3*(2*torch.rand(n)-1);

a = torch.tensor([2.,-3,1])
a = torch.nn.Parameter(a); a

lr = 1e-1

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X1,X2=np.meshgrid(x[:,0],x[:,1])
X3=np.ones([n,n])

Z=np.zeros([n,n])
ax.scatter(x[:,0],x[:,1],y);
ax.set_xlim(-1., 1.)
ax.set_ylim(-1., 1.)
ax.set_zlim(-15., 15.)
ax.set_xticks([-1. , -0.5 , 0.  , 0.5 , 1.  ])
ax.set_yticks([-1. , -0.5 , 0.  , 0.5 , 1.  ])
ax.set_zticks([-10. , -5.0,  0.  , 5.0, 10.  ])
for i in range(n):
    for j in range(n):
        Z[i,j]=X1[i,j]*a[0].detach().item()+X2[i,j]*a[1].detach().item()+X3[i,j]*a[2].detach().item()

text = ax.text2D(0.5, 0.8, '', transform=ax.transAxes)
plane = [ax.plot_surface(X1,X2,Z,cmap="magma" ,alpha=0.05)]
plt.close()

def animate(k):
    update()
    #find all predicted y values
    y_hat = x@a.detach()
    #calculate MSE loss
    loss = mse(y,y_hat)
    text.set_text('loss = %.1f' % loss.item())
    for i in range(n):
        for j in range(n):
            Z[i,j]=X1[i,j]*a[0].detach().item()+X2[i,j]*a[1].detach().item()+X3[i,j]*a[2].detach().item()
    plane[0].remove()
    plane[0] = ax.plot_surface(X1,X2,Z, cmap="magma",alpha=0.05)
    return text

animation.FuncAnimation(fig, animate, np.arange(0,100), interval=50)

