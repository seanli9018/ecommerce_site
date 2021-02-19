let data = [
  {
    'name': 'Gadget',
    'created_at': '2017-05-01'
  },
  {
    'name': 'Tiddlywink',
    'created_at': '2018-03-01'
  },
  {
    'name': 'Gizmo',
    'created_at': '2018-05-27'
  },
]

function createdMay(item) {
  let createTime = item.created_at
  let time_array = createTime.split('-');
  if(time_array[1] == '05'){
    return item
  }

}

let result = data.filter(createdMay)
console.log(result)