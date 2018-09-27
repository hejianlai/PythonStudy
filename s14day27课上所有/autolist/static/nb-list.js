/**
 * Created by Administrator on 2017/3/4.
 */
(function(jq){
        var requestURL;


        // 为字符串创建format方法，用于字符串格式化
        String.prototype.format = function (args) {
            return this.replace(/\{(\w+)\}/g, function (s, i) {
                return args[i];
            });
        };


        function init(){
            // 获取要显示的列
            // 获取数据
            $.ajax({
                url: requestURL,
                type:'GET',
                dataType: 'JSON',
                success:function(arg){
                    if(arg.status){
                        // 创建表格标题
                        createTablehead(arg.data.table_config);
                        /*
                        [{'port': 11, 'hostname': 'c1.com'}, {'port': 23, 'hostname': 'c2.com'}]
                         */

                        createTableBody(arg.data.table_config,arg.data.data_list);
                    }else{
                        alert(arg.message)
                    }
                }
            })
        }

        function createTablehead(config){
            /*
            tr
                td
                td
            tr
            [
                {
                    'title': '主机名',
                    'display':0,
                },
                {
                    'title': '端口',
                    'display':1,
                }
            ]
             */
            var tr = document.createElement('tr');
            $.each(config,function(k,v){
                if(v.display){
                    var th = document.createElement('th');
                    th.innerHTML = v.title;
                    $(tr).append(th);
                }
            });

            $('#thead').append(tr);
        }

        function createTableBody(tableConfig,dataList){
            /*
             dataList= [{'port': 11, 'hostname': 'c1.com'}, {'port': 23, 'hostname': 'c2.com'}]
             tableConfig = [
                {
                    'q': 'hostname',
                    'title': '主机名',
                    'display':0,
                },
                {
                    'q': 'port',
                    'title': '端口',
                    'display':1,
                },
                {
                    'q': None,
                    'title': '操作',
                    'display':1,
                }
            ]
             */
            $.each(dataList,function(k1,row){
                // row1= {'port': 11, 'hostname': 'c1.com'}
                // row2= {'port': 22, 'hostname': 'c2.com'}
                var tr = document.createElement('tr');

                $.each(tableConfig,function(k2,configItem){

                    if(configItem.display){
                        /*
                         configItem ={
                                'q': 'hostname',
                                'title': '主机名',
                                'display':0,
                                'text': {'content': '{n}-{m}','kwargs': {'n': 'hostname','m':'@id'}},
                                'attr': {'k1':'v'},
                            },
                         */
                        var td = document.createElement('td');
                        //td.innerHTML = row[configItem.q];
                        // configItem.text.content
                        var kwargs = {};
                        $.each(configItem.text.kwargs,function(key,value){
                            if(value.startsWith('@')){
                                var temp = value.substring(1,value.length);
                                kwargs[key]= row[temp]
                            }else{
                                kwargs[key]= value;
                            }
                        });
                        td.innerHTML = configItem.text.content.format(kwargs);

                        $.each(configItem.attr,function(key,value){
                            if(value.startsWith('@')){
                                var temp = value.substring(1,value.length);
                                td.setAttribute(key,row[temp]);
                            }else{
                                td.setAttribute(key,value);
                            }
                        });


                        $(tr).append(td);




                        }
                });

                $('#tbody').append(tr);

            })
        }

        jq.extend({
            'linan': function(url){
                requestURL = url;
                init();
            }


        })
})(jQuery);

