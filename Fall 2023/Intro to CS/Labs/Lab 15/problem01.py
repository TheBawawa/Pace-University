class Image:
  def __init__(self, file_name):
    file_data = open(file_name, 'r')
    lines = file_data.readlines()
    data_list = []

    for line in lines:
      list_line=line.split(',')
      data_list.append(list_line[1])

    self.user_name = data_list[0]
    self.url = data_list[1]
    metadata = []
  
    for i in range(len(data_list)):
      if i != 0 and i != 1:
        metadata.append(data_list[i])

    self.metadata = {
      "location": metadata[0], # this will be a string containing the image's geotag
      "tags": metadata[1], # this will include a string of tags separated by commas
      "is video?": metadata[2], # this can also be True if the post is in fact a video
      "time posted": metadata[3]} # this will actually be a number representing a time
    
  def upload(self,time):
    int_time = int(time)

    if int_time <= 2400:
      print("Upload successful!")
    else:
      print("Upload unsuccessful.")




random_image = Image('/Users/junjiequ/Desktop/Pace-University/Fall 2023/Intro to CS/Labs/Lab 15/lab15input.csv')
print(random_image.user_name)
random_image.upload(1800)
