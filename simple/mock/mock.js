import Mock from 'mockjs'

Mock.mock('/newlist/',{
    'list|5':[
        {
            url:'@url',
            title:'@ctitle(5.20)'
        }

    ]
})