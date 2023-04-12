import streamlit as st
import pickle
from keras.models import load_model
#model = load_model('./model.h5')
model=pickle.load(open('model.pkl','rb'))

def prediction(duration, protocol_type, service, flag, src_bytes,dst_bytes, wrong_fragment, hot, num_failed_logins, logged_in,num_compromised,
               num_root, num_file_creations,num_access_files, is_guest_login, count, srv_count,serror_rate, rerror_rate, same_srv_rate,diff_srv_rate,
               srv_diff_host_rate, dst_host_count, dst_host_srv_count,dst_host_diff_srv_rate, dst_host_same_src_port_rate,dst_host_srv_diff_host_rate,dst_host_rerror_rate):
    res=model.predict([[duration, protocol_type, service, flag, src_bytes,dst_bytes, wrong_fragment, hot, num_failed_logins, logged_in,num_compromised,
               num_root, num_file_creations,num_access_files, is_guest_login, count, srv_count,serror_rate, rerror_rate, same_srv_rate,diff_srv_rate,srv_diff_host_rate,
               dst_host_count, 
               dst_host_srv_count,
               dst_host_diff_srv_rate, 
               dst_host_same_src_port_rate,
               dst_host_srv_diff_host_rate,
               dst_host_rerror_rate]])
    return res

def main():
    st.title("INTRUSION DETECTION SYSTEM")
    html_temp = """
    <div style="background-color:#00ff00 ;padding:10px">
    <h2 style="color:white;text-align:center;">INTRUSION DETECTION</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    duration = st.text_input("Duration","Type Here")
    protocol_type=st.text_input("protocol_type","Type Here")
    service=st.text_input("service","Type Here")
    flag=st.text_input("flag","Type Here")
    src_bytes=st.text_input("src_bytes","Type Here")
    dst_bytes=st.text_input("dst_bytes","Type Here")
    wrong_fragment=st.text_input("wrong_fragment","Type Here")
    hot=st.text_input("hot","Type Here")
    num_failed_logins=st.text_input("num_failed_logins","Type Here")
    logged_in=st.text_input("logged_in","Type Here")
    num_compromised=st.text_input("num_compromised","Type Here")
    num_root=st.text_input("num_root","Type Here")
    num_file_creations=st.text_input("num_file_creations","Type Here")
    num_access_files=st.text_input("num_access_files","Type Here")
    is_guest_login=st.text_input("is_guest_login","Type Here")
    count=st.text_input("count","Type Here")
    srv_count=st.text_input("srv_count","Type Here")
    serror_rate=st.text_input("serror_rate","Type Here")
    rerror_rate=st.text_input("rerror_rate","Type Here")
    same_srv_rate=st.text_input("same_srv_rate","Type Here")
    diff_srv_rate=st.text_input("diff_srv_rate","Type Here")
    srv_diff_host_rate=st.text_input("srv_diff_host_rate","Type Here")
    dst_host_count=st.text_input("dst_host_count","Type Here")
    dst_host_srv_count=st.text_input("dst_host_srv_count","Type Here")
    dst_host_diff_srv_rate=st.text_input("dst_host_diff_srv_rate","Type Here")
    dst_host_same_src_port_rate=st.text_input("dst_host_same_src_port_rate","Type Here")
    dst_host_srv_diff_host_rate=st.text_input("dst_host_srv_diff_host_rate","Type Here")
    dst_host_rerror_rate=st.text_input("dst_host_rerror_rate","Type Here")
    

    safe_html="""  
      <div style="background-color:#32cd32;padding:10px >
       <h2 style="color:white;text-align:center;"> Your network is safe</h2>
       </div>
    """
    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> Attack detected !!!</h2>
       </div>
    """

    if st.button("Predict"):
        output=prediction(duration,protocol_type,service,flag,src_bytes,dst_bytes,wrong_fragment,hot,num_failed_logins,logged_in,num_compromised,num_root,num_file_creations,num_access_files,is_guest_login,count,srv_count,serror_rate,rerror_rate,same_srv_rate,diff_srv_rate,srv_diff_host_rate,dst_host_count,dst_host_srv_count,dst_host_diff_srv_rate,dst_host_same_src_port_rate,dst_host_srv_diff_host_rate,dst_host_rerror_rate)
        print(output)
        if output == 1:
            st.markdown(danger_html,unsafe_allow_html=True)
        else:
            st.markdown(safe_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()