# -*- coding: utf-8 -*-
#########################################################################
# File Name: ceshi1.py
# Author: arkulo
# mail: arkulo@163.com
#########################################################################
#!/usr/bin/python
import re
s='''<strong>中式针灸法提高生育能力</strong></p><p>这种被追捧的古老中医方法究竟有何魔力在美国盛行;使众多美国美容专家相信其神奇功效而相继上课，时下美国名媛们最热望实现的中式针灸医治包括了非手术紧肤、提高生育能力、治愈背疼等其他许许多多的高科技医术不能比拟的……</p><p>针灸，这个重新被追捧的古代保健方法，越来越被证明确实有提高生育能力的作用。历经千年之后，这个一度让我们联想到江湖郎中的神秘东方医术，凭借什么一夜之间赢得了大众的尊重呢?也许正是随着世界卫生组织和国家健康学会对针灸的疗效的报道，它就像一颗闪亮的新星逐渐进入全世界大众的视野。而明星效应，使它的光芒更加璀璨。从麦当娜到格温尼斯-帕特罗，明星们对它趋之若鹜，而且后者更是将爱情的美满也归功于它。</p><p><strong>温馨提示：</strong></p><p>针刺疗法基于传统中医理念，中医上说，健康由气而定，气是指一种在皮肤下活动的能量，包括同量的阴气和阳气。当这些气处于混乱状态时，人们就会感到不适，但是医生通过将细细的针插入体内，就可以帮助病人恢复适当的平衡。</p><p>针刺疗法也可能有助于缓解压力，因此可以提高怀孕几率。一些医生也表示，针刺疗法能增加子宫血液流动，帮助卵子更好地与精子结合。针刺疗法还能平衡体内激素水平。</p><p><strong>维生素E提高生育能力</strong></p><p>很多朋友尤其是男性朋友总抱怨生活的压力越发加大，一个男人承担着养家糊口的重任，尤其现在房价那么高，一些年轻的男士总是没日没夜的忙着赚钱，严重影响身体健康。这也是现在男士精子质量下降，不育男性增多很重要的原因。</p><p>男性想要保持健康的身体，就一定要注意日常保健。除了在饮食上多加注意外，维生素E也能帮助治疗男性不育。当男士缺乏维生素E时，引起睾丸损害，性功能减退与紊乱，容易出现精子运动异常或出现精子缺乏。对精子形成障碍患者，给予补充维生素E后，精液中的精子个数、运动性均有所改善，而且维生素E还有预防畸形胎形成的作用。</p><p>成人维生素E的适宜摄入量为每天10毫克，其中天然维生素E是可以长期适量服用的。一些因不育而烦恼的男士可以服用一些维生素，同时要在饮食中多食用莴笋、花生油等绿叶蔬菜和植物油。</p><p><strong>温馨提示：</strong></p><p>男性朋友还要注意，维生素E不能大量服用，每日定量即可，摄取过多就会中毒，如果服用它出现恶心之类不适症状的话，就说明你服用过量了。</p><p></p><divclass="insert_area"><ulclass="insert_piclist"><li>高晓松的宝宝</li><li>孩子的奇葩吃相</li><li>神奇宝宝创意摄影</li><li>宝宝哭相大PK</li></ul><ulclass="insert_artlist"><li>当孩子统治了这个世界</li><li>男性不育患癌风险高</li><liclass="redlist">食尚懒招大搜罗赢800元辅食</li><li>只想静静地看：婴儿百睡图</li><li>蜜一般的微笑甜到你心坎</li></ul></div><strong>食用特制的面包或提高生育能力</strong><p>在人体所需的微量元素中，硒元素可以增加男性的精子数量。科学家发现，成人每天应摄入60至70毫克硒，但事实上由于土壤矿物质贫乏等原因，人们每天摄入的硒含量还不到该标准的一半。如何才能提高人们对硒的摄入量?餐桌上的面包成为科学家眼中的最好载体。</p><p>科学家日前公布了一项研究成果，通过实验发明了一种可以增加小麦硒含量的肥料。用这种特殊肥料培育而成的小麦做成的面包，其硒含量将大大增加。因此，用这类小麦烤出的面包比一般面包更具“保健功能”。</p><p>研究人员首先开发出一种新型化肥，这种化肥能够提高小麦硒的含量，用这种小麦烤制</p><p>出的面包硒含量比普通面包高。微量元素硒对精子的形成和成熟起着重要作用，它能增强精子活力，防止精子过早解体，有利于精子与卵子结合，对人类生育具有重大影响。</p><p><strong>温馨提示：</strong></p><p>硒是一种矿物质，人体需要它来实现许多细胞功能，而且它也有抗氧化剂的性质。确保每天要摄取所推荐的每日硒元素许可量，但不要过量。'''

r = re.compile("<divclass=\"insert_area\">.*?</div>")

match=r.search(s)
if(match):
    print match.group()
else:
    print "no"
