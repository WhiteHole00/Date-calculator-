def main():
        day_ = input("시작 날짜를 적어주세요. (ex. 3/1 >> ")
        end_ = input("끝 날짜를 적어주세요. (ex. 12/25 >> ")
        try:
            start_month =int(day_.split("/")[0])
            start_day = int(day_.split("/")[1])
            end_month =int(end_.split("/")[0])
            end_day =int(end_.split("/")[1])
            a = [0,31,28,31,30,31,30,31,31,30,31,30,31]
            cnt = 0
            cnt_ = 0
            for i in range(1,start_month):
                cnt += a[i]
            cnt += start_day

            for j in range(1,end_month):
                cnt_ += a[j]
            cnt_ += end_day

            result = ""
            result = f"{start_month}월 {start_day}일 부터 {end_month}월 {end_day}일까지는 '{cnt_-cnt}'일 남았습니다!"

            return print(result)
        except Exception as e:
            return input("아무키나 누르면 종료 됩니다")
if __name__ == "__main__":
    main()
