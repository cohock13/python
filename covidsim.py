import math
from typing import List
from random import random,uniform
from enum import Enum,auto

class State(Enum):
        Normal = auto()
        Infected = auto()
        Recovered = auto()
        Dead = auto()

class Cell(object):
    #感染半径
    R = 1.0
    #感染確率
    INF_RATE = 0.9
    #回復率
    RECOV_RATE = 0.02
    #死亡率
    DEATH_RATE = 0.002

    def __init__(self,state:State,vel:tuple,bounding:tuple):
        super().__init__()
        self.pos = uniform(*(bounding[0])),uniform(*(bounding[1]))
        self.vel = vel
        self.bounding = bounding
        self.state = state
        self._next_state_ = state

    #感染判定
    def infection(self,cell)->bool:
        #相手が感染済みでないなら処理無し
        if cell.state != State.Infected:
            return False

        #そうでない場合, 自分が健康であるとき
        if self.state == State.Normal:
            d = math.dist(self.pos,cell.pos)
            p = random()
            if d<Cell.R and p<Cell.INF_RATE:
                self._next_state_ = State.Infected
                return True
        
        return False

    #回復判定
    def recovery(self)->bool:
        #もし自分が感染していないなら処理なし
        if self.state != State.Infected:
            return True

        #そうでない場合
        #死亡判定
        p = random()
        if p < Cell.DEATH_RATE:
            self._next_state_ = State.Dead
            return False
        #回復判定
        p = random()
        if p < Cell.RECOV_RATE:
            self._next_state_ = State.Recovered
            return True

        return False

    def update(self):
        pos = self.update_pos()
        state = self.update_state()
        return pos,state

    #移動速度の変更
    def update_vel(self):
        if self.state == State.Dead:
            self.vel = 0.0,0.0
    #位置の移動
    def update_pos(self)->tuple:
        #内部存在判定関数
        def is_unbounded(x,y):
            (xmin,xmax),(ymin,ymax) = self.bounding
            return not xmin<=x<=xmax,not ymin<=y<=ymax
        
        #範囲内への丸め込み関数
        def clamp():
            #内部で呼ばれる丸め込み関数
            def _clmp_(value,bound):
                vmin,vmax = bound
                if vmin <= value <= vmax:
                    return value
                if value < vmin:
                    return vmin
                if vmax < value:
                    return vmax
            self.pos = tuple(map(lambda x: _clmp_(x[0],x[1]),zip(self.pos,self.bounding)))
        
        x,y = self.pos
        vx,vy = self.vel
        self.pos = x+vx,y+vy
            
        #移動方向の反転判定
        x_unbound,y_unbound = is_unbounded(x,y)
        if x_unbound and y_unbound:
            self.vel = -vx,-vy
        if x_unbound:
            self.vel = -vx,vy
        if y_unbound:
            self.vel = vx,-vy

        #丸め込み
        clamp()
        return self.pos

    #状態の遷移
    def update_state(self):
        self.state = self._next_state_
        return self.state


class Simulator(object):
    def __init__(self,maxbounding):
        self.cells:List[Cell] = []
        self.maxbounding = maxbounding
        (xmin,xmax),(ymin,ymax) = maxbounding
        self.boundlength = min(xmax-xmin,ymax-ymin)

    def add_cell(self,state:State,vel:tuple,bounding:tuple = None):
        if bounding is None:
            bounding = self.maxbounding

        self.cells.append(Cell(state,vel,bounding))

    def add_cells(self,num:int,staterate:float,v:float,maxboundlen=None,minv=None):
        if maxboundlen is None or self.boundlength<maxboundlen:
            maxboundlen = self.boundlength

        if minv is None:
            minv = v

        #引数の計算関数
        def calc_arg()->tuple:
            #速度計算
            #移動方向の決定
            rad = 2.0*math.pi*random()
            #速さの決定
            speed = uniform(minv,v)
            #速度の決定
            vel = speed*math.cos(rad),speed*math.sin(rad)

            #移動範囲(boundingbox)計算
            xmin,ymin = tuple(
                map(lambda a:uniform(a[0],a[1]-maxboundlen),
                self.maxbounding))
            bounding = (xmin,xmin+maxboundlen),(ymin,ymin+maxboundlen)
            return vel,bounding
        
        #感染者数の決定(切り上げ)
        n_infected = -(int(-num*staterate))
        for _ in range(n_infected):
            self.add_cell(State.Infected,*calc_arg())
            
        for _ in range(n_infected,num):
            self.add_cell(State.Normal,*calc_arg())

    def simulate(self,maxstep = 1000):
        for _ in range(maxstep):
            self.step()

    def step(self):
        #感染判定
        for c in self.cells:
            for e in self.cells:
                c.infection(e)
        #回復判定, 移動処理
        for c in self.cells:
            c.recovery()
            c.update()
            