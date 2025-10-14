import mujoco
import mujoco.viewer
import threading

def run_viewer(model, data):
    with mujoco.viewer.launch_passive(model, data) as viewer:
        while viewer.is_running():
            mujoco.mj_step(model, data)
            viewer.sync()

def main():

    type = input("Enter '0' for right hand, '1' for left hand, '2' for both: ")
    
    if type == '0':
        model_r = mujoco.MjModel.from_xml_path('model/rohand_lites_right.xml')
        data_r = mujoco.MjData(model_r)
        run_viewer(model_r, data_r)
    elif type == '1':
        model_l = mujoco.MjModel.from_xml_path('model/rohand_lites_left.xml')
        data_l = mujoco.MjData(model_l)
        run_viewer(model_l, data_l)
    elif type == '2':
        model_r = mujoco.MjModel.from_xml_path('model/rohand_lites_right.xml')
        data_r = mujoco.MjData(model_r)
        model_l = mujoco.MjModel.from_xml_path('model/rohand_lites_left.xml')
        data_l = mujoco.MjData(model_l)

        t1 = threading.Thread(target=run_viewer, args=(model_r, data_r))
        t2 = threading.Thread(target=run_viewer, args=(model_l, data_l))

        t1.start()
        t2.start()
        t1.join()
        t2.join()

if __name__ == "__main__":
    main()