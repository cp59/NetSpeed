from flask import Flask,render_template,request,flash,send_file
app=Flask("main")
@app.route("/")
def index():
    return render_template("index.html")
dlp="D:\\NetSpeedSampleFiles"
@app.route("/download/100mb")
def dl30mb():
    return send_file(dlp+"\\100mb.zip",as_attachment=True)
upload="D:\\NetSpeedSampleFiles"
@app.route("/upload",methods=["POST"])
def upload():
    try:
        f = request.files['file']
        f.save("D:\\"+f.filename)
    except:
        pass
    return 'file uploaded successfully'
@app.route("/emptyData")
def emptyData():
    return ""

app.run(host="0.0.0.0",port=8080,debug=True,threaded=True)
