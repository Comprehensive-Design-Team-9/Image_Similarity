import data_load_save
import knn_match
import time

start = time.time()

img_path = "../Web_Crawler/data/naver_blog_post_img" + "/"
csv_path = "data/final_20211207121745.csv"
save_csv_path = "./data/test_imgSM_submission.csv"
tmp_list = []
img_path_list = []
all_img_list = []
similarity_stack = []
post_sm_cost = []
sum_sm_data = []

if __name__ == "__main__":
    print("Run")
    data_load_save.read_submission_csv(tmp_list, csv_path)
    print("csv url loaded")
    # print(tmp_list[1])
    # print(tmp_list[2])
    data_load_save.make_csv(["url", "similarity cost"], save_csv_path)
    tmp_list.pop(0)
    print("Get jpg path")
    for i in tmp_list:
        img_path_list = data_load_save.load_img_path(img_path, i)
        # print("img_list : ", img_list)
        # print("img path")
        for j in img_path_list:
            all_img_list.append(i+"/"+j)
    # print(all_img_list)
    print("Start knn", len(all_img_list))
    num = 0
    for p in tmp_list:
        print(num, " : ", p)
        num += 1
        for q in all_img_list:
            for k in all_img_list:
                sm_data = knn_match.knn_match_fun(q, k)
                similarity_stack.append(sm_data)
            sum_sm_data.append(sum(similarity_stack))
            similarity_stack.clear()
        data_load_save.save_similarity_csv([p, f"{sum(sum_sm_data)-1/len(sum_sm_data)-1}"], save_csv_path)
        sum_sm_data.clear()
        print(time.time()-start/60)

    print("Finish", time.time()-start/60)
