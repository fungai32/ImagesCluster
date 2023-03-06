import pandas as pd

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    all_clusters=pd.read_csv('./static/datasets/cluster_images.csv')
    all_clusters.drop(columns='product_category',inplace=True)
    filtering_array=all_clusters.Images_Cluster.unique()
    all_cluster_images_lists=[]#list of list#list of list
    for cluster_id in filtering_array:
        cluster_data=[]
        cluster=all_clusters[all_clusters.Images_Cluster==cluster_id]
        image_data=[]
        for article_id in range(len(cluster)):
            image_data.append(cluster.iloc[article_id])
        cluster_data.append(image_data)  
        all_cluster_images_lists.append(cluster_data)    
   
    return render_template('index.html',clusters=all_cluster_images_lists)

def return_all_clusters():
    all_clusters=pd.read_csv('./static/datasets/cluster_images.csv')
    all_clusters.drop(columns='product_category',inplace=True)
    filtering_array=all_clusters.Images_Cluster.unique()
    all_cluster_images_lists=[]#list of list#list of list
    for cluster_id in filtering_array:
        cluster_data=[]
        cluster=all_clusters[all_clusters.Images_Cluster==cluster_id]
        image_data=[]
        for article_id in range(len(cluster)):
            image_data.append(cluster.iloc[article_id])
        cluster_data.append(image_data)  
        all_cluster_images_lists.append(cluster_data)  
    return all_cluster_images_lists

@app.route('/single_cluster/<id>')
def single_cluster(id):
    all_clusters=pd.read_csv('./static/datasets/cluster_images.csv')
    cluster_id=int(id)#star variable
    cluster_data=[]
    cluster=all_clusters[all_clusters.Images_Cluster==cluster_id]
    article_data=[]
    for article_id in range(0,len(cluster)):
        article_data.append(cluster.iloc[article_id].tolist())
    cluster_data.append(article_data)  
    list(cluster_data)
    set_pair=[(0,5),(5,10),(10,15),(15,20),(25,30),(30,35),(35,40),(45,50),
              (50,55),(55,60),(60,65),(65,70),(75,80),(85,90),(95,100)
              ]
    my_clusters=return_all_clusters()
    cluster_size=len(cluster_data[0])
    return render_template('single_cluster.html',single_cluster=cluster_data,set_pair=set_pair,cluster_id=cluster_id,clusters=my_clusters,cluster_size=cluster_size)

app.add_url_rule('/', 'index', index)
app.add_url_rule('/single_cluster', 'single_cluster', single_cluster)


#if __name__ == '__main__':
#    app.run()
