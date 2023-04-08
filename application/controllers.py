from flask import Flask, redirect, render_template, request, current_app as app
from flask_login import login_required, current_user, login_user, logout_user
from application.models import User, db,Venue,show,Review
from application.models import booking
from datetime import datetime
@app.route('/admin')
def admin():
    return render_template('adminlogin.html')

# @app.route('/adminauth',methods=['POST'])
# def adminauth():
#     if request.method=='POST':
# @app.route('/admindasboard',methods=['GET'])
# def admindashboard():
#     if request.method=='GET':
#         venuelist=Venue.query.all()
#         return render_template('addashboard.html',venues=venuelist)
@app.route('/userlogin')
def userlogin():
	return render_template('userlogin.html')

@app.route('/login',methods=['POST','GET'])
def login():
     if request.method=='POST':
        email = request.form['email']
        user = User.query.filter_by(email = email).first()
        if user is not None and user.password==request.form['password']:
            # login_user(user)
            if user.isAdmin:
                venuelist=Venue.query.all()
                shows=[]
                for thisvenue in venuelist:
                    showlist=show.query.filter_by(venue_Id=thisvenue.id)
                    shows.append(showlist)
                
                return render_template('addasboard.html',venues=venuelist,shows=shows) 
            # return render_template('dashboard.html')     
            venuelist=Venue.query.all()
            shows=[]
            for thisvenue in venuelist:
                showlist=show.query.filter_by(venue_Id=thisvenue.id)
                shows.append(showlist)
                
            return render_template('userdashboard.html',venues=venuelist,shows=shows,email=email) 
     return render_template('login.html')     
 
# @app.route('/login', methods = ['POST', 'GET'])
# def login():
#     if current_user.is_authenticated:
#         return redirect('userdashboard.html')
     
#     if request.method == 'POST':
#         email = request.form['email']
#         user = User.query.filter_by(email = email).first()
#         if user is not None and user.check_password(request.form['password']):
#             login_user(user)
#             return redirect('userdashboard.html')
     
#     return render_template('userlogin.html')

@app.route('/userregister', methods=['POST', 'GET'])
def userregister():
     
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
 
        # if User.query.filter_by(email=email):
        #     return ('Email already Present')
             
        user = User(email=email, username=username, password=password, name=username,isAdmin=False)
        # user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('userregister.html')
	

# @app.route('/userregister')
# def userregister():
# 	return render_template('userregister.html') 


@app.route("/", methods=["GET", "POST"])
def dashboard():
    return render_template("dashboard.html")

#@app.route("/articles_by/<user_name>", methods=["GET", "POST"])
#@login_required
#def articles_by_author(user_name):
    #articles = Article.query.filter(Article.authors.any(username=user_name))
    #return render_template("articles_by_author.html", articles=articles, username=user_name)

@app.route('/createvenue', methods=['GET'])
def create_venue():
    # if request.method=='POST':
    #     name = request.form['name']
    #     place = request.form['place']
    #     capacity = request.form['capacity']
    #     # id = request.form['id']

    #     venue = Venue( name=name, user_id=2, place=place, capacity=capacity)
    #     db.session.add(venue)
    #     db.session.commit()
    #     return render_template('addasboard.html')
    if request.method=='GET':
        return render_template('venuead.html')
    return 'Venue created successfully!'    
@app.route('/addvenue', methods=['POST'])
def add_venue():
    if request.method=='POST':
        name = request.form['name']
        place = request.form['place']
        capacity = request.form['capacity']
        # id = request.form['id']

        venue = Venue( name=name, user_Id=2, place=place, capacity=capacity)
        db.session.add(venue)
        db.session.commit()
        venuelist=Venue.query.all()
        shows=[]
        for thisvenue in venuelist:
                    showlist=show.query.filter_by(venue_Id=thisvenue.id)
                    shows.append(showlist)
                
        return render_template('addasboard.html',venues=venuelist,shows=shows) 
        # return render_template('addasboard.html',venues=venuelist)
@app.route('/editvenue/<int:venue_id>/', methods=['POST','GET'])
def edit_venue(venue_id):
    if request.method=='POST':
        id = venue_id
        venue = Venue.query.get(id)

        if venue:
            venue.name = request.form['name']
            venue.place = request.form['place']
            venue.capacity = request.form['capacity']
            db.session.commit()
            thisvenue=Venue.query.all()
            return render_template('addasboard.html',venues=thisvenue)
        # return 'Venue updated successfully!'
        else:
            return 'Venue not found.'
    
    if request.method=='GET':
        thisvenue=Venue.query.filter_by(id=venue_id).first()
        return render_template('editvenue.html',venue=thisvenue)
@app.route('/deletevenue/<int:venue_id>/', methods=['GET','POST'])
def delete_venue(venue_id):
    id = venue_id
    venue = Venue.query.get(id)

    if venue:
        db.session.delete(venue)
        db.session.commit()
        delvenue=Venue.query.all()
        return render_template('addasboard.html',venues=delvenue)
    else:
        return 'Venue not found.'

@app.route('/createshow/<int:venue_id>/', methods=['GET'])
def create_show(venue_id):
    if request.method=='GET':
        return render_template('showad.html',venue=venue_id)
    return 'Show created successfully!'    

@app.route('/addshow/<int:venue_id>/', methods=['POST'])
def add_show(venue_id):
    if request.method=='POST':
        name = request.form['showname']
        tags=request.form['tags']
        # date = request.form['date']
        start_time = datetime.strptime(request.form['start_time'],"%Y-%m-%dT%H:%M")
        end_time=datetime.strptime(request.form['end-time'],"%Y-%m-%dT%H:%M")
        date=start_time
        tprice=request.form['ticket-price']
        # id = request.form['id']

        sh = show( name=name, user_Id=2, ticket_price=tprice,startTime=start_time,endTime=end_time,date=date,venue_Id=venue_id,tags=tags)
        db.session.add(sh)
        db.session.commit()
        venuelist=Venue.query.all()
        shows=[]
        for thisvenue in venuelist:
                    showlist=show.query.filter_by(venue_Id=thisvenue.id)
                    shows.append(showlist)
                
        return render_template('addasboard.html',venues=venuelist,shows=shows) 
        # venuelist=Venue.query.all()
        # return render_template('addasboard.html',venues=venuelist)
@app.route('/deleteshow/<int:show_id>/', methods=['GET','POST'])
def delete_show(show_id):
    id = show_id
    se = show.query.get(id)

    if se:
        db.session.delete(se)
        db.session.commit()
        venuelist=Venue.query.all()
        shows=[]
        for thisvenue in venuelist:
            showlist=show.query.filter_by(venue_Id=thisvenue.id)
            shows.append(showlist)
                
        return render_template('addasboard.html',venues=venuelist,shows=shows) 
        # delse=show.query.all()
        # return render_template('addasboard.html',shows=delse)
    else:
        return 'show not found.'  
   
@app.route('/editshow/<int:show_id>/', methods=['POST','GET'])
def edit_show(show_id):
    if request.method=='POST':
        id = show_id
        se = show.query.get(id)
        if se:
            se.name = request.form['name']
            se.startTime =datetime.strptime(request.form['start_time'],"%Y-%m-%dT%H:%M")
            se.endTime = datetime.strptime(request.form['end_time'],"%Y-%m-%dT%H:%M")
            se.ticket_price=request.form['price']
            db.session.commit()
        venuelist=Venue.query.all()
        shows=[]
        for thisvenue in venuelist:
            showlist=show.query.filter_by(venue_Id=thisvenue.id)
            shows.append(showlist)
                
        return render_template('addasboard.html',venues=venuelist,shows=shows) 
        # delse=show.query.all()
        # return render_template('addasboard.html',shows=delse)
    else:
        thisshow=show.query.filter_by(id=show_id).first()
        return render_template('editshow.html',show=thisshow)
        return 'show not found.' 
    
@app.route("/booking/<int:show_id>/",methods=['GET','POST'])
def userbooking(show_id):
    id=show_id
    # user_id=current_user.id
    if request.method=='GET':
        thiscapacity=0
        newshow=show.query.filter_by(id=show_id).first()
        newlist=Venue.query.all()
        for thisvenue in newlist:
            if thisvenue.id==newshow.venue_Id:
                thiscapacity=thisvenue.capacity
        newbookinglist=booking.query.all()
        for thisbooking in newbookinglist :
            if thisbooking.show_id==show_id:
                thiscapacity-=thisbooking.count
        if thiscapacity==0:
            return render_template('housefull.html')              
        return render_template('booking.html',show_id=id,seatsleft=thiscapacity)
    if request.method=='POST':
        ticket=request.form['ticket']
        email=request.form['email']
        thisuser=User.query.filter_by(email=email).first()
        thisbooking=booking(show_id=id,user_id=thisuser.id,count=int (ticket))
        db.session.add(thisbooking)
        db.session.commit()
        venuelist=Venue.query.all()
        shows=[]
        for thisvenue in venuelist:
            showlist=show.query.filter_by(venue_Id=thisvenue.id)
            shows.append(showlist)
                
        return render_template('userdashboard.html',venues=venuelist,shows=shows,email=email) 


@app.route("/mybookings/<email>/",methods=['GET'])
def mybookings(email):
    thisuser=User.query.filter_by(email=email).first()
    bookings=booking.query.filter_by(user_id=thisuser.id)
    showlist={}
    for thisbooking in bookings:
        thisshow=show.query.filter_by(id=thisbooking.show_id).first()
        showlist[thisbooking.id]=thisshow
    return render_template('mybookings.html',bookings=bookings,shows=showlist,user_id=thisuser.id)    

@app.route("/ratingshow/<int:show_id>/<int:user_id>/",methods=['GET','POST'])
def ratingshow(show_id,user_id):
    if request.method=='POST':
        rating=request.form['rating']
        thisrating=Review(rating=rating,show_Id=show_id,user_Id=user_id)
        db.session.add(thisrating)
        db.session.commit()
        return render_template("thanks.html")
    else :

        return render_template('rating.html',show_id=show_id,user_id=user_id)
    
@app.route('/showanalytics/<int:show_id>/',methods=['GET'])
def showanalytics(show_id):
    if request.method=='GET':
        rateshow= show.query.filter_by(id=show_id).first()   
        ratingslist=Review.query.all()
        ratingoutput=[0,0,0,0,0]
        for ra in ratingslist:
            if ra.show_Id==show_id:
                ratingoutput[ra.rating-1]+=1
        return render_template("analytics.html",rating_list=ratingoutput,show=rateshow)    

@app.route("/search_shows",methods=['GET'])
def search_shows():
    seshow=show.query.all()
    return render_template("search.html",showlist=seshow)     

@app.route("/search",methods=['GET','POST'])
def search():
    searchtext=request.form['search']
    search = "%{}%".format(searchtext)
    showlist = show.query.filter(show.name.like(search)).all()
    showtags = show.query.filter(show.tags.like(search)).all()
    return render_template("search.html",showlist=showlist,showtags=showtags)





