#!/usr/bin/python3
import yaml
import sys

def change_deployment_tag(file, tag):
  try:
    #Opening a file(manifest) on which the tag should be changed.
    with open(str(file)) as deployment:
      #Getting current deployment from file.
      current_deployment                                                       = yaml.safe_load(deployment)
      #Getting the full image name with tag from the `current_deployment` variable.
      current_deployment_image_with_tag                                        = current_deployment['spec']['template']['spec']['containers'][0]['image']
      #Getting only the image name, not the tag, from `current_deployment_image_with_tag` variable.
      image                                                                    = current_deployment_image_with_tag.split(':')[0]
      #Creating new full image with tag, which(tag) will be passed from the `tag` variable
      new_image                                                                = str(image + ':' + tag)
      #Merging new image to the deployment.
      current_deployment['spec']['template']['spec']['containers'][0]['image'] = new_image
    #Opening the old deployment file to write new changes.
    with open(str(file), 'w') as new_deployment:
      #Writing on the file the latest generated deployment by this script with the newer version of image tag.
      new_deployment.write(yaml.dump(current_deployment))
  except:
    print("Unable to change deployment image.")

def main(file, tag):
    change_deployment_tag(file, tag)

#sys.argv[1] = file
#sys.argv[2] = tag
main(sys.argv[1], sys.argv[2])
