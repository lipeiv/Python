# bundle_id = input("请输入bundle_id：")

# if bundle_id is not None and  bundle_id.strip() != "":
# 	bundle_id = bundle_id.strip()
# 	print(bundle_id, len(bundle_id))
# else:
# 	print("bundle_id为空！")


# app = {"name": "ios", "bundle_id": bundle_id}

# if app["bundle_id"] is None or app["bundle_id"].strip() == "":
# 	print("字典中bundle_id为空！")
# else:
# 	print("字典中bundle_id为:", app["bundle_id"])

bundleid = [{"bundle":None}, {"bundle":'valuepush'}, {"bundle":''}]

for i in bundleid:
	if not i['bundle']:
		print("Error")