import json
ROOM = """
["room_id":13861,"room_name":"\u4e0d\u4e8c\uff1a6\u865a\u70752\u547c\u5566","room_gg":{"show":"<p>\n\t<u>\u6bcf\u5929\u65e9\u4e0a8\u70b9\u524d\u5f00\u64ad\uff01\u4e0d\u4e8c\u7089\u77f3\u4ea4\u6d411\u7fa4\uff1a165639187\uff08\u6ee1\uff09\uff0c2\u7fa4316573039(\u6ee1\uff093\u7fa4<\/u><span style=\"line-height:1.5;\"><span style=\"font-size:14px;line-height:29px;\"><u>79357726\uff08\uff094\u7fa4390296456\uff08\u6ee1\uff095\u7fa4161444828\uff08\u6ee1\uff09<\/u><\/span><\/span><u>\uff0c\u5361\u7ec4\u5728\u7fa4\u6587\u4ef6\uff0c\u9700\u8981\u7684\u6c34\u53cb\u81ea\u884c\u4e0b\u8f7d<\/u>\n<\/p>\n<p>\n\t<u>\u65b0\u6d6a\u5fae\u535a\uff1a\u6597\u9c7c\u4e36\u4e0d\u4e8c<\/u>\n<\/p>\n<p>\n\t<u>\u5e05\u9192\u53ea\u662f\u4e00\u79cd\u6001\u5ea6\uff0c\u5e76\u4e0d\u4ee3\u8868\u4e3b\u64ad\u6709\u591a\u5e05\uff0c\u8fd8\u6709\uff0c\u4e3b\u64ad\u83dc\u7684\u62a0\u811a\uff01<\/u>\n<\/p>","status":"1","pass":True,"verify":""},"room_pic":"http:\/\/rpic.douyucdn.cn\/z1604\/10\/15\/13861_160410155758.jpg","owner_uid":336068,"owner_name":"\u4e0d\u4e8c","show_status":1,"room_url":"http:\/\/www.douyu.com\/room\/share\/13861","show_id":11270907,"room_pwd":0,"cate_id":2,"cate_name":"\u7089\u77f3\u4f20\u8bf4","cate_url":"\/directory\/game\/How","near_show_time":"1456791000","game_cate_list":{"1":"\u82f1\u96c4\u8054\u76df","2":"\u7089\u77f3\u4f20\u8bf4","3":"DOTA2","33":"\u7a7f\u8d8a\u706b\u7ebf","5":"\u9b54\u517d\u4e16\u754c","148":"\u5b88\u671b\u5148\u950b","190":"\u7687\u5ba4\u6218\u4e89","4":"\u661f\u9645\u4e89\u9738","29":"\u683c\u6597\u6e38\u620f","19":"\u4e3b\u673a\u6e38\u620f","40":"\u5730\u4e0b\u57ce\u4e0e\u52c7\u58eb","172":"\u9c7c\u884c\u5929\u4e0b","30":"\u7efc\u5408\u624b\u6e38","132":"\u5168\u6c11\u661f\u79c0","133":"\u5143\u6c14\u9886\u57df","188":"\u9c7c\u79c0","173":"\u5c0f\u9c9c\u8089","26":"\u6000\u65e7\u6e38\u620f","35":"\u98ce\u66b4\u82f1\u96c4","196":"\u706b\u5f71\u5fcd\u8005\u624b\u6e38","51":"\u8db3\u7403\u7ade\u6280","117":"Music+","159":"\u65f6\u5c1a\u5236\u9020","11":"\u4f7f\u547d\u53ec\u5524OL","59":"\u5929\u6daf\u660e\u6708\u5200","72":"SNH48","6":"CS:GO","174":"\u6b21\u5143\u58c1\u5792","55":"\u9b54\u517d\u4e89\u9738","175":"\u9c7c\u97f3\u7ed5\u6881","90":"\u8dd1\u8dd1\u5361\u4e01\u8f66","157":"\u8bdb\u4ed93","46":"\u9006\u6218","155":"\u7bee\u7403\u6e38\u620f","134":"\u73a9\u6570\u7801","136":"\u73a9\u6c7d\u8f66","193":"\u73a9VR","115":"\u73a9\u91d1\u878d","8":"\u4f53\u80b2\u9891\u9053","7":"AKB48","14":"\u4e09\u56fd\u6740","24":"\u795e\u4e4b\u6d69\u52ab","161":"\u865a\u8363","62":"\u7f51\u6e38\u524d\u77bb","116":"HEX","111":"\u684c\u6e38\u5bc6\u5ba4","158":"\u4e43\u6728\u574246","147":"\u9ad8\u8fbe\u6587\u5316\u533a","48":"300\u82f1\u96c4","32":"\u6697\u9ed1\u7834\u574f\u795e3","182":"\u76f4\u51fb\u73b0\u573a","65":"\u5251\u7f513","183":"\u56fd\u6f2b","13":"\u5251\u7075","184":"\u5973\u56e2","113":"\u68cb\u724c\u5a31\u4e50","185":"\u7f51\u7edc\u70ed\u95e8","160":"\u638c\u673a\u6e38\u620f","54":"\u97f3\u4e50\u6e38\u620f","66":"\u53cd\u6050\u7cbe\u82f1","23":"\u9965\u8352","57":"\u884c\u661f\u8fb9\u96452","97":"\u51b3\u6218\u82cd\u7a79","61":"\u75be\u98ce\u4e4b\u5203","47":"\u7ade\u901f\u6e38\u620f","63":"\u9b54\u57df","12":"\u8d85\u795e\u82f1\u96c4","60":"\u795e\u8c15\u4e4b\u6218","77":"\u82f1\u9b42\u4e4b\u5203","80":"\u4e5d\u9634\u771f\u7ecf","15":"\u6fc0\u62182","86":"\u6218\u5730\u4e4b\u738b","87":"\u7fa4\u96c4\u9010\u9e7f","88":"\u5c04\u96d5ZERO","89":"\u738b\u724c\u5bf9\u51b3","95":"\u5168\u7403\u4f7f\u547d","114":"\u7a81\u51fb\u82f1\u96c4","41":"\u6700\u7ec8\u5e7b\u60f314","101":"\u5929\u4e4b\u7981","69":"\u68a6\u5e7b\u897f\u6e38","105":"\u5929\u8c15","106":"\u9f99\u4e4b\u8c37","108":"\u82f1\u96c4\u7687\u51a0","109":"\u6218\u8230\u4e16\u754c","82":"\u7b2c\u4e09\u628a\u5251","83":"\u68a6\u4e09\u56fd2","112":"\u53cd\u6050\u7cbe\u82f1OL2","78":"\u68a6\u5854\u9632","79":"\u6d41\u653e\u4e4b\u8defPOE","119":"\u65e0\u51acOL","122":"\u6218\u4e89\u96f7\u9706","123":"\u5168\u6c11\u8d85\u795e","126":"\u661f\u9645\u6218\u7532","127":"\u4e0a\u53e4\u4e16\u7eaa","128":"\u82f1\u96c4\u4e09\u56fd","129":"\u50cf\u4e09\u56fd","130":"\u9f99\u7ffc\u7f16\u5e74\u53f2","142":"\u5766\u514b\u4e16\u754c","143":"\u5f81\u90142\u52a8\u4f5c\u7248","38":"\u4e09\u56fd\u4e89\u97382","44":"\u6211\u7684\u4e16\u754c","163":"\u8f69\u8f95\u4f20\u59472","164":"\u602a\u7269\u730e\u4ebaol","165":"\u5168\u804c\u5927\u5e08","167":"\u6c38\u6052\u4e4b\u5854","170":"\u65b0\u5929\u9f99\u516b\u90e8","186":"\u795e\u9014","187":"\u4f20\u5947","189":"\u4f20\u5947\u6c38\u6052","137":"\u79d1\u5b66\u63a2\u7d22","177":"\u90e8\u843d\u51b2\u7a81","194":"\u9752\u9752\u6821\u56ed","195":"\u9c7c\u6559\u9c7c\u4e50","178":"CF\u67aa\u6218\u738b\u8005","179":"\u68a6\u5e7b\u897f\u6e38\u624b\u6e38","180":"\u5929\u5929\u9177\u8dd1","181":"\u738b\u8005\u8363\u8000","162":"CIBN","191":"\u81ea\u7531\u4e4b\u6218","192":"\u7403\u7403\u5927\u4f5c\u6218"},"all_tag_list":{"4":{"name":"\u989c\u503c\u7206\u8868","count":"26846"},"6":{"name":"\u65b0\u79c0","count":"66627"},"12":{"name":"\u5fa1\u5b85\u8fbe\u4eba","count":"20792"},"15":{"name":"\u4e8c\u6b21\u5143","count":"8753"},"18":{"name":"\u6597\u9c7c\u58f0\u4f18","count":"11468"},"23":{"name":"\u57df\u5916\u98ce\u60c5","count":"3856"},"42":{"name":"\u8d5b\u4e8b\u76f4\u64ad","count":"3938"},"43":{"name":"\u4eba\u5728\u65c5\u9014","count":"7191"},"46":{"name":"\u56db\u56fd\u519b\u68cb","count":"271"},"47":{"name":"\u82f1\u96c4\u6740","count":"524"},"68":{"name":"\u4e0a\u6d77\u7279\u9526\u8d5b","count":"60"},"69":{"name":"\u9c7c\u884c\u5929\u4e0b","count":"3420"},"48":{"name":"CDEC\u8054\u8d5b","count":"124"},"8":{"name":"\u804c\u4e1a\u9009\u624b","count":"6415"},"20":{"name":"\u6e38\u620f\u5973\u795e","count":"4799"},"34":{"name":"\u738b\u8005\u5927\u817f","count":"6624"},"33":{"name":"\u4e0a\u5206\u8fbe\u4eba","count":"12628"},"3":{"name":"\u56fd\u670d\u7b2c\u4e00","count":"12608"},"30":{"name":"\u7ca5\u91cc\u6709\u6bd2","count":"11036"},"31":{"name":"\u82b1\u5f0f\u7ade\u6280\u573a","count":"4394"},"32":{"name":"\u5929\u68af\u51b2\u51fb","count":"3882"},"40":{"name":"\u795e\u62bdDog","count":"2372"},"71":{"name":"\u9c9c\u8089\u76f4\u64ad","count":"5931"},"53":{"name":"\u5200\u59b9\u840c\u65b0","count":"611"},"54":{"name":"\u65b0\u664b\u4e3b\u64ad","count":"22588"},"55":{"name":"\u5200\u5854RPG","count":"728"},"56":{"name":"\u5929\u68af\u9ad8\u73a9","count":"554"},"57":{"name":"\u7edd\u6d3b\u54e5","count":"2459"},"72":{"name":"\u624b\u64ad\u8fbe\u4eba","count":"3424"},"19":{"name":"\u97f3\u4e50\u7535\u53f0","count":"9471"},"64":{"name":"\u661f\u9645\u8c10\u4f1a","count":"473"},"65":{"name":"\u5373\u65f6\u6218\u7565","count":"1228"},"52":{"name":"\u5fb7\u5dde\u6251\u514b","count":"330"},"9":{"name":"\u6211\u662f\u6b4c\u624b","count":"12471"},"13":{"name":"\u6280\u672f\u6d41","count":"29459"},"24":{"name":"\u5f71\u89c6\u5929\u5802","count":"10234"},"49":{"name":"moba\u624b\u6e38","count":"613"},"27":{"name":"\u5361\u724c\u7ade\u6280","count":"3953"},"41":{"name":"\u6597\u9c7c\u6bd2\u5976","count":"10954"},"25":{"name":"\u89d2\u8272\u626e\u6f14","count":"9794"},"26":{"name":"\u7b56\u7565\u7ecf\u8425","count":"3238"},"35":{"name":"GTA5","count":"2668"},"36":{"name":"\u9a6c\u91cc\u5965","count":"917"},"37":{"name":"\u6050\u6016\u6e38\u620f","count":"2900"},"59":{"name":"FC\u6bc1\u7ae5\u5e74","count":"707"},"60":{"name":"\u8857\u673a\u5236\u9738","count":"387"},"62":{"name":"\u7ea2\u8272\u8b66\u6212","count":"191"},"63":{"name":"\u5e1d\u56fd\u65f6\u4ee3","count":"93"},"74":{"name":"\u94a2\u94c1\u5c11\u5973","count":"175"},"75":{"name":"\u95ee\u9053","count":"60"},"76":{"name":"\u8230\u5a18","count":"80"},"77":{"name":"\u6597\u5730\u4e3b\u624b\u6e38","count":"65"}},"room_tag_list":["40","31","30","4","3"],"show_time":1460272706,"can_send_gift":"{\"is_white_list\":false,\"credit\":12,\"stop_gift_credit\":4}","member_credit_enable":True,"child_id":"0","isshow":0,"widgetType":0,"widgetPosition":0]
"""
r=json.dumps(ROOM)

print(r)