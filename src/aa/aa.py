# """
# （1）考虑了与障碍物安全距离
# （2）采用16邻域
# （3）采用对角线距离
# （4）转弯成本
# （5）考虑障碍物分布
# （6）采用正反Floyd算法进行平滑
# （7）考虑不同路面情况
# """

import random
import math

###############构造地图################
#宽高W，H。
class Array2D:
    #初始化
    def __init__(self,w,h):
        self.w=w
        self.h=h
        self.data=[]
        self.data=[[0.0 for y in range(h)] for x in range(w)]
 
    #显示地图
    def showArray2D(self):
        for y in range(self.h):
            for x in range(self.w):
                print(self.data[x][y],end=' ')
            print("")
    
    #获得任意节点信息 ，__getitem__()魔法函数作用为当实例化对象map进行map[key]操作上自动调用。
    def __getitem__(self, item):
        return self.data[item]

###############创建点类################
class Point:
    #初始化
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    #判断是否同一个点
    def __eq__(self, other):
        if self.x==other.x and self.y==other.y:
            return True
        return False
    
    #打印点信息
    def __str__(self):
        return "x:"+str(self.x)+",y:"+str(self.y)
    
###############创建A-Star类############
class AStar:
    
    # 描述AStar算法中的节点数据
    class Node:  
        #初始化
        def __init__(self, point, startPoint,endPoint, g=0,w=1,p=1):
            self.point = point  # 自己的坐标
            self.father = None  # 父节点
            self.g = g       # g值，g值在用到的时候会重新算
            
            # 计算h值，采用曼哈顿距离
            #self.h = (abs(endPoint.x - point.x) + abs(endPoint.y - point.y)) * 10  
            
            #采用欧几里得距离
            #self.h = math.pow((math.pow((endPoint.x - point.x),2) + math.pow((endPoint.y - point.y),2)),0.5)*10
            
            #采用对角距离
            pp=(1-p)+0.2*math.exp((math.pow((math.pow((endPoint.x - point.x),2) + math.pow((endPoint.y - point.y),2)),0.5))/(math.pow((math.pow((endPoint.x - startPoint.x),2) + math.pow((endPoint.y - startPoint.y),2)),0.5)))
            Diagonal_step = min((endPoint.x - point.x),(endPoint.y - point.y))
            straight_step = (abs(endPoint.x - point.x) + abs(endPoint.y - point.y)) - 2*Diagonal_step
            self.h  =(straight_step + math.pow(2,0.5)*Diagonal_step)*10*pp
            #print(pp)


            
    #初始化A-start
    def __init__(self, map2d, startPoint, endPoint, passTag=1.0):#map2d地图信息，startPoint起点, endPoint终点, passTag=1.0为不可行驶区域

        # 开启表
        self.openList = []
        # 关闭表
        self.closeList = []
        # 寻路地图
        self.map2d = map2d
        # 起点终点
        if isinstance(startPoint, Point) and isinstance(endPoint, Point):
            self.startPoint = startPoint
            self.endPoint = endPoint
        else:
            self.startPoint = Point(*startPoint)
            self.endPoint = Point(*endPoint)
 
        # 不可行走标记
        self.passTag = passTag
 
    def getMinNode(self):
        """
        获得openlist中F值最小的节点
        :return: Node
        """
        currentNode = self.openList[0]
        for node in self.openList:
            if node.g + node.h < currentNode.g + currentNode.h:
                currentNode = node
        return currentNode#返回最小代价的点
    
    #判断节点是否在关闭表中
    def pointInCloseList(self, point):
        for node in self.closeList:
            if node.point == point:
                return True
        return False
    
    #判断节点是否在开启表中，是返回该节点
    def pointInOpenList(self, point):
        for node in self.openList:
            if node.point == point:
                return node
        return None
    
    #判断开启表中是否有终点
    def endPointInCloseList(self):
        for node in self.openList:
            if node.point == self.endPoint:
                return node
        return None
    
    
    #方向标签
    def Angle(self,point_father,point_son):
        if point_son.x-point_father.x==0 and point_son.y-point_father.y==-1:
            angle=1
            return angle
        if point_son.x-point_father.x==1 and point_son.y-point_father.y==-2:
            angle=2
            return angle
        if point_son.x-point_father.x==1 and point_son.y-point_father.y==-1:
            angle=3
            return angle
        if point_son.x-point_father.x==2 and point_son.y-point_father.y==-1:
            angle=4
            return angle
        if point_son.x-point_father.x==1 and point_son.y-point_father.y==0:
            angle=5
            return angle
        if point_son.x-point_father.x==2 and point_son.y-point_father.y==1:
            angle=6
            return angle
        if point_son.x-point_father.x==1 and point_son.y-point_father.y==1:
            angle=7
            return angle
        if point_son.x-point_father.x==1 and point_son.y-point_father.y==2:
            angle=8
            return angle
        if point_son.x-point_father.x==0 and point_son.y-point_father.y==1:
            angle=9
            return angle
        if point_son.x-point_father.x==-1 and point_son.y-point_father.y==2:
            angle=10
            return angle
        if point_son.x-point_father.x==-1 and point_son.y-point_father.y==1:
            angle=11
            return angle
        if point_son.x-point_father.x==-2 and point_son.y-point_father.y==1:
            angle=12
            return angle
        if point_son.x-point_father.x==-1 and point_son.y-point_father.y==0:
            angle=13
            return angle
        if point_son.x-point_father.x==-2 and point_son.y-point_father.y==-1:
            angle=14
            return angle
        if point_son.x-point_father.x==-1 and point_son.y-point_father.y==-1:
            angle=15
            return angle
        if point_son.x-point_father.x==-1 and point_son.y-point_father.y==-2:
            angle=16
            return angle

    #转弯惩罚系数
    def constant (self,angle_main,angle_son):
        diff=abs(angle_main-angle_son)
        if diff==12:
            diff=4
        if diff==13:
            diff=3
        if diff==14:
            diff=2
        if diff==15:
            diff=1 
           
        if diff==0:
            turn_cost=1
        if diff==1:
            turn_cost=1.2
        if diff==2:
            turn_cost=1.4
        if diff==3:
            turn_cost=1.6
        if diff==4:
            turn_cost=1.8
        
        if diff>4:
            turn_cost=10000
    
        return turn_cost
    
    
    #障碍物分布
    def obstacle_dis(self,minF):
        if minF.father==None:
            return 1
        angle=self.Angle(minF.father.point,minF.point)#主方向   
        #print(angle)

        if angle==1:
            x_left=minF.point.x-2
            x_right=minF.point.x+2
            y_up=minF.point.y-5

            if x_left<0:
                x_left=0
            if x_right>(w-1):
                x_right=(w-1)
            if y_up<0:
                y_up=0

            N=0#障碍物数
            s=0#总网格数
            
            for i in range(x_left,x_right+1):
                for j in range(y_up,minF.point.y+1):
                    s=s+1
                    N=N+map2d[i][j]

            P0=N/s#障碍率
            #print(P0)
            #print(N)
            #print(s)
            return P0

        if angle==5:
            x_right=minF.point.x+5
            y_up=minF.point.y-2
            y_dowm=minF.point.y+2

            if x_right>(w-1):
                x_right=(w-1)
            if y_up<0:
                y_up=0
            if y_dowm>(h-1):
                y_dowm=(h-1)
            N=0#障碍物数
            s=0#总网格数
            for i in range(minF.point.x,x_right+1):
                for j in range(y_up,y_dowm+1):
                    s=s+1
                    N=N+map2d[i][j]
            P0=N/s#障碍率
            return P0

        if  angle==9:
            x_left=minF.point.x-2
            x_right=minF.point.x+2
            y_dowm=minF.point.y+5

            if x_left<0:
                x_left=0
            if x_right>(w-1):
                x_right=(w-1)
            if y_dowm>(h-1):
                y_dowm=(h-1)

            N=0#障碍物数
            s=0#总网格数
            for i in range(x_left,x_right+1):
                for j in range(minF.point.y,y_dowm+1):
                    s=s+1
                    N=N+map2d[i][j]

            P0=N/s#障碍率
            return P0

        if angle==13:
            x_left=minF.point.x-5
            y_up=minF.point.y-2
            y_dowm=minF.point.y+2

            if x_left<0:
                x_left=0
            if y_up<0:
                y_up=0
            if y_dowm>(h-1):
                y_dowm=(h-1)
            N=0#障碍物数
            s=0#总网格数
            for i in range(x_left,minF.point.x+1):
                for j in range(y_up,y_dowm+1):
                    s=s+1 
                    N=N+map2d[i][j]

            P0=N/s#障碍率

            #print(P0)
            #print(N)
            #print(s)
            return P0

        if angle==2 or angle==3 or angle==4:
            x_right=minF.point.x+5
            y_up=minF.point.y-5

            if x_right>(w-1):
                x_right=(w-1)
            if y_up<0:
                y_up=0
            N=0#障碍物数
            s=0#总网格数
            for i in range(minF.point.x,x_right+1):
                for j in range(y_up,minF.point.y+1):
                    s=s+1
                    N=N+map2d[i][j]

            P0=N/s#障碍率
            return P0

        if angle==6 or angle==7 or angle==8:
            x_right=minF.point.x+5
            y_dowm=minF.point.y+5

            if x_right>(w-1):
                x_right=(w-1)
            if y_dowm>(h-1):
                y_dowm=h-1
            N=0#障碍物数
            s=0#总网格数
            for i in range(minF.point.x,x_right+1):
                for j in range(minF.point.y,y_dowm+1):
                    s=s+1
                    N=N+map2d[i][j]

            P0=N/s#障碍率
            return P0

        if angle==10 or angle==11 or angle==12:
            x_left=minF.point.x-5
            y_dowm=minF.point.y+5

            if x_left<0:
                x_right=0
            if y_dowm>(h-1):
                y_dowm=h-1
            N=0#障碍物数
            s=0#总网格数
            for i in range(x_left,minF.point.x+1):
                for j in range(minF.point.y,y_dowm+1):
                    s=s+1
                    N=N+map2d[i][j]

            P0=N/s#障碍率
            return P0

        if angle==14 or angle==15 or angle==16:
            x_left=minF.point.x-5
            y_up=minF.point.y-5

            if x_left<0:
                x_right=0
            if y_up<0:
                y_dowm=0
            N=0#障碍物数
            s=0#总网格数
            for i in range(x_left,minF.point.x+1):
                for j in range(y_up,minF.point.y+1):
                    s=s+1
                    N=N+map2d[i][j]

            P0=N/s#障碍率
            #print(N)
            #print(s)
            return P0

    
    #搜索16方位的节点
    def searchNear(self, minF, offsetX, offsetY):
        """
        搜索节点周围的点
        :param minF:F值最小的节点
        :param offsetX:坐标偏移量
        :param offsetY:
        :return:
        """
        # 越界检测
        if minF.point.x + offsetX < 0 or minF.point.x + offsetX > self.map2d.w - 1 or minF.point.y + offsetY < 0 or minF.point.y + offsetY > self.map2d.h - 1:
            return
        
        # 如果是障碍，就忽略
        if self.map2d[minF.point.x + offsetX][minF.point.y + offsetY] == self.passTag:
            return 
        
        #对于对角，如果邻域是障碍物，就忽略
        if self.map2d[minF.point.x + offsetX][minF.point.y ] == self.passTag or self.map2d[minF.point.x ][minF.point.y+ offsetY] == self.passTag:
            return
        
        #对于大斜对角，如果邻域是障碍物，就忽略
        if abs(offsetX)==1 and abs(offsetY)==2:
            if offsetY>0:
                if self.map2d[minF.point.x ][minF.point.y +1 ] == self.passTag:
                    return
                if self.map2d[minF.point.x+offsetX ][minF.point.y +1 ] == self.passTag:
                    return           
            if offsetY<0:
                if self.map2d[minF.point.x ][minF.point.y +(-1)] == self.passTag:
                    return
                if self.map2d[minF.point.x+offsetX ][minF.point.y +(-1)] == self.passTag:
                    return
                            
        if abs(offsetX)==2 and abs(offsetY)==1:
            if offsetX>0:
                if self.map2d[minF.point.x +1][minF.point.y ] == self.passTag:
                    return
                if self.map2d[minF.point.x +1][minF.point.y +offsetY] == self.passTag:
                    return
                
            if offsetX<0:
                if self.map2d[minF.point.x +(-1)][minF.point.y ] == self.passTag:
                    return
                if self.map2d[minF.point.x +(-1)][minF.point.y +offsetY] == self.passTag:
                    return
                
        
        # 如果在关闭表中，就忽略
        currentPoint = Point(minF.point.x + offsetX, minF.point.y + offsetY)#节点位置
        if self.pointInCloseList(currentPoint):
            return
        
        # 设置单位花费
        if offsetX == 0 or offsetY == 0:
            step = 10#横向代价为10
        if abs(offsetX )== 1 and abs(offsetY )== 1:
            step = 14#斜向代价为14
        if abs(offsetX )== 2 or abs(offsetY )== 2:
            step = 22#大斜向代价为22
        
        
        #转弯代价
        if minF.father==None:
            turn_cost=1
        else:
            main_angle=self.Angle(minF.father.point,minF.point)#主方向
            angle_son=self.Angle(minF.point, currentPoint)#当前方向
            
            #转弯代价
            turn_cost=self.constant (main_angle,angle_son)
            
            if turn_cost>1.8:
                turn_cost=1000
                
            step=step*turn_cost
            #print(step)
            
        #路面类别惩罚
       
        road_cost=1+self.map2d[minF.point.x + offsetX][minF.point.y + offsetY]
        step=step*road_cost#权值
        #step=step+step*road_cost
            
        #障碍率
        P0=self.obstacle_dis(minF)
        #print(P0)
            
        # 如果不再openList中，就把它加入openlist
        currentNode = self.pointInOpenList(currentPoint)#判断节点是否在开启表中，纯在返回该节点，不存在返回None
        if not currentNode:
            currentNode = AStar.Node(currentPoint, self.startPoint,self.endPoint, g=minF.g + step,w=turn_cost,p=P0)#计算g值，为父节点g+横向/斜向代价
            currentNode.father = minF        #将minF设置为该节点的父节点
            self.openList.append(currentNode)#添加进开启表
            return
        
        # 如果在openList中，判断minF到当前点的G是否更小
        if minF.g + step < currentNode.g:  # 如果更小，就重新计算g值，并且改变father
            currentNode.g = minF.g + step#从新计算g
            currentNode.father = minF#将minF设置为该节点的新的父节点
 
    def start(self):
        """
        开始寻路
        :return: None或Point列表（路径）
        """
        # 判断寻路终点是否是障碍
        if self.map2d[self.endPoint.x][self.endPoint.y] == self.passTag:
            return None
 
        # 1.将起点放入开启列表
        startNode = AStar.Node(self.startPoint,startPoint, self.endPoint)
        self.openList.append(startNode)
        
        # 2.主循环逻辑
        while True:
            
            # 找到F值最小的点
            minF = self.getMinNode()
            
            # 把这个点加入closeList中，并且在openList中删除它
            self.closeList.append(minF)
            self.openList.remove(minF)
            
            # 判断这个节点的左右上下边角节点              
            self.searchNear(minF, 0, -1)
            self.searchNear(minF, 0, 1)
            self.searchNear(minF, -1, 0)
            self.searchNear(minF, 1, 0)            
            
            #判断这个节点的对角边角节点 
            self.searchNear(minF, 1, -1)
            self.searchNear(minF, -1, 1)
            self.searchNear(minF, -1, -1)
            self.searchNear(minF, 1, 1)
            
            
            #添加大方向角点
            self.searchNear(minF, 1, 2)
            self.searchNear(minF, 2, 1)
            self.searchNear(minF, -1, 2)
            self.searchNear(minF, -2, 1)
            self.searchNear(minF, 1, -2)
            self.searchNear(minF, 2, -1)
            self.searchNear(minF, -1, -2)
            self.searchNear(minF, -2, -1)
            
    
            # 判断是否终止
            point = self.endPointInCloseList()
            if point:  # 如果终点在关闭表中，就返回结果
                cPoint = point
                pathList = []#路径表
                while True:
                    if cPoint.father:
                        pathList.append(cPoint.point)#将当前点的父节点添加路径表
                        cPoint = cPoint.father       #将父节点设置为当前点
                    else:
                        return list(reversed(pathList)),self.closeList,self.openList
            
            #如果开启表为空，返回无路径，防止死循环
            if len(self.openList) == 0:
                return None

#正向 Floyd算法           
def Floyd(startPoint,endPoint,pathList):

    S1=[]
    currentpoint=startPoint
    S1.append(currentpoint)
    if pathList[0].x-currentpoint.x!=0:
        angle=abs(pathList[0].y-currentpoint.y)/abs(pathList[0].x-currentpoint.x)
        b=pathList[0].y - angle*pathList[0].x
    else:
        angle =2
        b=22

    for i in range(1,len(pathList)):
        if pathList[i].x-currentpoint.x!=0:

            angle_=abs(pathList[i].y-currentpoint.y)/abs(pathList[i].x-currentpoint.x)
            b_=pathList[i].y - angle*pathList[i].x
        else:
            angle_=1000
            b_=10000

        if angle!=angle_ and b!=b_:  
            currentpoint= pathList[i-1]
            S1.append(pathList[i-1])
            if pathList[i].x-currentpoint.x!=0:
                angle=abs(pathList[i].y-currentpoint.y)/abs(pathList[i].x-currentpoint.x)
                b=pathList[i].y - angle*pathList[i].x
            else:
                angle=1000
                b=10000        
    S1.append(endPoint)
    S2=[]
    S2.append(S1[0])
    start=S1[0]
    for i in range(1,len(S1)):

        if start.x<=S1[i].x:
            up_x=start.x
            dowm_x=S1[i].x
        else:
            up_x=S1[i].x
            dowm_x=start.x

        if start.y<=S1[i].y:
            up_y=start.y
            dowm_y=S1[i].y
        else:
            up_y=S1[i].y
            dowm_y=start.y
        
        if S1[i].x-start.x!=0:
            A=abs((S1[i].y-start.y)/(S1[i].x-start.x))
            B=-1
            C=S1[i].y-A*S1[i].x
                
            for xx in range(up_x,dowm_x+1):
                for yy in range(up_y,dowm_y+1):
                    if map2d[xx][yy]==1:
                        D=abs(A*xx+B*yy+C)/math.pow((A*A+B*B),0.5)*map2d[xx][yy]
                        if D<math.pow(8,0.5):
                            S2.append(S1[i-1])
                            start=S1[i-1]
        if S1[i].x-start.x==0:
            for xx in range(up_x,dowm_x+1):
                for yy in range(up_y,dowm_y+1):
                    if map2d[xx][yy]==1:
                        D=abs(xx-S1[i].x)*map2d[xx][yy]
                        if D<math.pow(8,0.5):
                            S2.append(S1[i-1])
                            start=S1[i-1]

        if S1[i].y-start.y==0:
            for xx in range(up_x,dowm_x+1):
                for yy in range(up_y,dowm_y+1):
                    if map2d[xx][yy]==1:
                        D=abs(yy-S1[i].y)*map2d[xx][yy]
                        if D<math.pow(8,0.5):
                            S2.append(S1[i-1])
                            start=S1[i-1]
    S2.append(S1[-1])
    return S1 ,S2


#反向Floyd
def Floyd_r(startPoint,pathList):
    S1=[]
    currentpoint=pathList[0]
    S1.append(currentpoint)
    if pathList[1].x-currentpoint.x!=0:
        angle=abs(pathList[1].y-currentpoint.y)/abs(pathList[1].x-currentpoint.x)
        b=pathList[1].y - angle*pathList[1].x
    else:
        angle =2
        b=22

    for i in range(2,len(pathList)):
        if pathList[i].x-currentpoint.x!=0:

            angle_=abs(pathList[i].y-currentpoint.y)/abs(pathList[i].x-currentpoint.x)
            b_=pathList[i].y - angle*pathList[i].x
        else:
            angle_=1000
            b_=10000

        if angle!=angle_ and b!=b_:  
            currentpoint= pathList[i-1]
            S1.append(pathList[i-1])
            if pathList[i].x-currentpoint.x!=0:
                angle=abs(pathList[i].y-currentpoint.y)/abs(pathList[i].x-currentpoint.x)
                b=pathList[i].y - angle*pathList[i].x
            else:
                angle=1000
                b=10000        
    S1.append(startPoint)
    S2=[]
    S2.append(S1[0])
    start=S1[0]
    for i in range(1,len(S1)):
        if start.x<=S1[i].x:
            up_x=start.x
            dowm_x=S1[i].x
        else:
            up_x=S1[i].x
            dowm_x=start.x

        if start.y<=S1[i].y:
            up_y=start.y
            dowm_y=S1[i].y
        else:
            up_y=S1[i].y
            dowm_y=start.y
        if S1[i].x-start.x!=0 :
            A=abs((S1[i].y-start.y)/(S1[i].x-start.x))
            B=-1
            C=S1[i].y-A*S1[i].x
            for xx in range(up_x,dowm_x+1):
                for yy in range(up_y,dowm_y+1):
                    if map2d[xx][yy]!=0:
                        D=abs(A*xx+B*yy+C)/math.pow((A*A+B*B),0.5)*map2d[xx][yy]
                        if D<math.pow(2,0.5):
                            S2.append(S1[i-1])
                            start=S1[i-1]
        if S1[i].x-start.x==0:
            for xx in range(up_x,dowm_x+1):
                for yy in range(up_y,dowm_y+1):
                    if map2d[xx][yy]!=0:
                        D=abs(xx-S1[i].x)*map2d[xx][yy]
                        if D<math.pow(2,0.5):
                            S2.append(S1[i-1])
                            start=S1[i-1]

        if S1[i].y-start.y==0:
            for xx in range(up_x,dowm_x+1):
                for yy in range(up_y,dowm_y+1):
                    if map2d[xx][yy]!=0:
                        D=abs(yy-S1[i].y)*map2d[xx][yy]
                        if D<math.pow(2,0.5):
                            S2.append(S1[i-1])
                            start=S1[i-1]
    S2.append(S1[-1])
    
    return S1 ,S2



#############测试##############
if __name__ == '__main__':
    
    #创建一个10*10的地图
    w=35
    h=30
    map2d=Array2D(w,h)
    startPoint=Point(0,0)
    endPoint  =Point(34,0)  
    import numpy as np

    #设置随机障碍物
    obstacle_num=300
    for i in range(obstacle_num):  # 循环obstacle_num次  随机生成障碍
        x = random.randint(0, (w-1))
        y = random.randint(0, (h-1))
        map2d[x][y]=1
        if x==startPoint.x and y==startPoint.y:
            map2d[x][y]=0
        if x==endPoint.x and y==endPoint.y:
            map2d[x][y]=0
      
    #设置障碍（地图一）

    
    map2d=Array2D(w,h)
    for x in range(4,20):
        for y in range(0,13):
            map2d[x][y]=1
    for x in range(0,18):
        for y in range(16,20):
            map2d[x][y]=1
    for x in range(25,30):
        for y in range(5,20):
            map2d[x][y]=1
    """
    """ 
    #设置障碍（地图二）       
    for x in range(5,25):
        for y in range(5,15):
            map2d[x][y]=1
    for x in range(14,16):
        for y in range(2,15):
            map2d[x][y]=1
    for x in range(7,23):
        for y in range(15,17):
            map2d[x][y]=1
    for x in range(9,21):
        for y in range(17,18):
            map2d[x][y]=1
   
    #地图三
    for x in range(4,20):
        for y in range(0,13):
            map2d[x][y]=1
    for x in range(0,18):
        for y in range(16,20):
            map2d[x][y]=1
    for x in range(25,30):
        for y in range(5,20):
            map2d[x][y]=1
    for x in range(0,15):
        for y in range(0,7):
            map2d[x][y]=0
           
    #地图四
    for x in range(15,20):
        for y in range(0,13):
            map2d[x][y]=1
    for x in range(0,18):
        for y in range(16,20):
            map2d[x][y]=1
    for x in range(25,30):
        for y in range(5,20):
            map2d[x][y]=1 
    for x in range(6,20):
        for y in range(6,7):
            map2d[x][y]=1
    for x in range(8,10):
        for y in range(11,18):
            map2d[x][y]=1
           
    #地图五       
    for x in range(15,20):
        for y in range(0,13):
            map2d[x][y]=1
    for x in range(0,18):
        for y in range(16,20):
            map2d[x][y]=1
    for x in range(25,30):
        for y in range(5,20):
            map2d[x][y]=1 
    for x in range(6,20):
        for y in range(6,7):
            map2d[x][y]=1
    for x in range(8,10):
        for y in range(11,18):
            map2d[x][y]=1 
    for x in range(0,8):
        for y in range(3,4):
            map2d[x][y]=1 
    for x in range(19,20):
        for y in range(13,15):
            map2d[x][y]=1
    for x in range(24,30):
        for y in range(2,3):
            map2d[x][y]=1
    for x in range(22,25):
        for y in range(9,10):
            map2d[x][y]=1
    
      
    #大地图
    for i in range(0,20):
        for j in range(22,23):
            map2d[i][j]=1

    for i in range(25,30):
        for j in range(22,23):
            map2d[i][j]=1

    for i in range(30,31):
        for j in range(0,23):
            map2d[i][j]=1

    for i in range(10,30):
        for j in range(12,13):
            map2d[i][j]=1

    for i in range(0,45):
        for j in range(35,36):
            map2d[i][j]=1
    
    for i in range(7,8):
        for j in range(0,8):
            map2d[i][j]=1 
    
    for i in range(4,8):
        for j in range(3,4):
            map2d[i][j]=1 
    
    
    #路面分类地图1
    for i in range(0,13):
        for j in range(20,30):
            map2d[i][j]=0.7

    for i in range(4,8):
        for j in range(15,20):
            map2d[i][j]=1.0

    for i in range(2,7):
        for j in range(0,13):
            map2d[i][j]=0.8       

    for i in range(5,8):
        for j in range(0,10):
            map2d[i][j]=1.0

    for i in range(17,30):
        for j in range(0,12):
            map2d[i][j]=0.2

    for i in range(10,17):
        for j in range(10,17):
            map2d[i][j]=0.8

    for i in range(17,27):
        for j in range(22,30):
            map2d[i][j]=0.5

    for i in range(17,30):
        for j in range(15,17):
            map2d[i][j]=1.0

    for i in range(10,15):
        for j in range(2,8):
            map2d[i][j]=1.0
            
      
    #分类地图2
    for i in range(3,7):
        for j in range(0,22):
            map2d[i][j]=1.0

    for i in range(4,14):
        for j in range(18,28):
            map2d[i][j]=0.2        
    for i in range(5,13):
        for j in range(19,27):
            map2d[i][j]=0.4
    for i in range(6,12):
        for j in range(20,26):
            map2d[i][j]=0.6    
    for i in range(7,11):
        for j in range(21,25):
            map2d[i][j]=0.8
    for i in range(8,10):
        for j in range(22,24):
            map2d[i][j]=1.0

    for i in range(9,18):
        for j in range(0,14):
            map2d[i][j]=0.5

    for i in range(15,18):
        for j in range(16,30):
            map2d[i][j]=1.0

    for i in range(22,26):
        for j in range(0,22):
            map2d[i][j]=1.0

    for i in range(28,32):
        for j in range(17,30):
            map2d[i][j]=1.0

    for i in range(25,35):
        for j in range(5,15):
            map2d[i][j]=0.2        
    for i in range(26,34):
        for j in range(6,14):
            map2d[i][j]=0.4        
    for i in range(27,33):
        for j in range(7,13):
            map2d[i][j]=0.6
    for i in range(28,32):
        for j in range(8,12):
            map2d[i][j]=0.8
    for i in range(29,31):
        for j in range(9,11):
            map2d[i][j]=1.0
    
    #创建AStar对象
    aStar=AStar(map2d,startPoint,endPoint)
    
    #开始寻路
    pathList,closeList,openList=aStar.start()
    
    #Floyd算法平滑路径
    S1 ,S2=Floyd(startPoint,endPoint,pathList)
    
    #反向Floyd算法
    pathList_r=pathList
    pathList_r.reverse()
    S1_r,S2_r=Floyd_r(startPoint,pathList_r)
    
    
    """
    #记录遍历的点
    for node in closeList:
        map2d[node.point.x][node.point.y]="sss"#算法遍历范围
    for node in openList:
        map2d[node.point.x][node.point.y]="sss"#算法遍历范围
    """ 
    #遍历路径点,在map2d上以'*'显示
    
    for points in pathList:
        map2d[points.x][points.y]="***"
    
    for points in S1:
        map2d[points.x][points.y]="!!!"
    
    for points in S2:
        map2d[points.x][points.y]="HHH"
    
    
    map2d[startPoint.x][startPoint.y]="AAA"#起点
    map2d[endPoint.x][endPoint.y]="TTT"    #终点
    #print("----------------------")
    
    #显示地图
    map2d.showArray2D()
    
    print(len(closeList)+len(openList))
