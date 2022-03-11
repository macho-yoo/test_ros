# test_ros

실행하는 각 파일의 이름은 problem_n.py 와 같은 형식으로 작성 부탁드립니다.
실행하는 launch 파일의 이름은 problem_n.launch 로 작성부탁드립니다.

1. String Type으로 “Today is 2022-03-08, Hello World” 를 /new_msg 라는 토픽으로
Publish하는 코드를 작성하시오 (problem_1.py)

2. Turtlesim을 켜고, Turtlesim의 거북이를 0.5m/s, 1,0rad/s로 움직일 수 있는 토픽을
Publish하는 코드를 작성하시오 (problem_2.py)

3. PolygonStamped Type으로 별을 그리는 코드를 작성하시오, 크기는 상관 없으며,
2차원에서 그리면 됩니다. Rviz를 통해 확인할 수 있도록 해주세요. (problem_3.py)

4. Marker Type 3개를 포함하는 MarkerArray Type을 Publish합니다.
각 Marker는 Cube, Sphere, Cylinder를 포함해야합니다.(각 1개)
시간에 따라 색깔이 변하도록 작성해주세요. (5가지 이상으로 변하도록, 반복해서)
Rviz 상에서 확인할 수 있도록 해주세요. (problem_4.py)

5. Turtlesim을 켜고, Turtlesim의 /turtle1/pose를 Subscribe하는 코드를 작성하세요.
최종 출력은 “(x, y, theta) = (0.0, 0.2, 0.5)” 와 같은 형태가 되도록 해주세요.
(problem_5.py)

6. Simulator를 켜고, /lidar2D 을 받아서, range가 제일 가까운 위치의 각도를
출력해주는 코드를 작성하세요.
최종 출력은 “minimum ranges’ (0.5m) angle is 15.3 degree” 와 같은 형태로
해주세요.

7. Simulator를 켜고, /cmd_vel 으로 0.5m/s, 0.0rad/s 로 이동할 수 있도록 명령을
보내고, /lidar2D를 받아서, 차량 전방 1m 이내에 물체가 있을 경우, 정지하도록
해주세요.

8. turtlesim을 켭니다
python의 raw_input 함수를 이용하여, 숫자 2개를 입력으로 받습니다.
입력받은 두 숫자를 (x, y)로 하여, (x, y)로 이동하는 코드를 작성하세요.
(turtlesim의 pose를 입력으로 받고, cmd_vel로 데이터를 보내서 목표 장소로 이동할
수 있도록 작성하면 됩니다.)

9. rosrun turtlesim turtlesim_node
rosrun turtlesim draw_square
