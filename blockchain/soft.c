#define _CRT_SECURE_NO_WARNINGS 1
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAXSIZE 100
typedef struct
{
    int id;
    char name[10];
    int score;
}student;
typedef struct
{
    student data[MAXSIZE];
    int last;
}sequenlist;
int Createlist(sequenlist* L) {
    L = (sequenlist*)malloc(sizeof(sequenlist));
    L->last = -1;
    return 1;
}
int Insertlist(sequenlist* L, student data, int i) {
    int j;
    if (L->last == MAXSIZE - 1) {
        return 0;
    }
    if (i < 0 || i > L->last + 1) {
        return 1;
    }
    for (j = L->last; j >= i; j--) {
        L->data[j + 1] = L->data[j];
    }
    L->data[i] = data;
    L->last++;
    return 2;
}
int Deletelist(sequenlist* L, int i) {
    int j;
    if (i < 0 || i > L->last) {
        return 0;
    }
    for (j = i; j < L->last; j++) {
        L->data[j] = L->data[j + 1];
    }
    L->last--;
    return 1;
}
int Getlist(sequenlist* L, int i, student* data) {
    if (i < 0 || i > L->last) {
        return 0;
    }
    *data = L->data[i];
    return 1;
}
int Reverselist(sequenlist* L) {
    int last = L->last;
    if (last == -1 || last == 0) {
        return 0;
    }
    int i;
    int mid = last / 2;
    student temp;
    for (i = 0; i <= mid; i++) {
        temp = L->data[i];
        L->data[i] = L->data[last - i];
        L->data[last - i] = temp;
    }
    return 1;
}
void sortById(sequenlist* L) {
    for (int i = 0; i <= L->last - 1; i++) {
        for (int j = 0; j <= L->last - i - 1; j++) {
            if (L->data[j].id > L->data[j + 1].id) {
                student temp = L->data[j];
                L->data[j] = L->data[j + 1];
                L->data[j + 1] = temp;
            }
        }
    }
}
void sortByName(sequenlist* L) {
    for (int i = 0; i <= L->last - 1; i++) {
        for (int j = 0; j <= L->last - i - 1; j++) {
            if (strcmp(L->data[j].name, L->data[j + 1].name) > 0) {
                student temp = L->data[j];
                L->data[j] = L->data[j + 1];
                L->data[j + 1] = temp;
            }
        }
    }
}
void sortByScore(sequenlist* L) {
    for (int i = 0; i <= L->last - 1; i++) {
        for (int j = 0; j <= L->last - i - 1; j++) {
            if (L->data[j].score > L->data[j + 1].score) {
                student temp = L->data[j];
                L->data[j] = L->data[j + 1];
                L->data[j + 1] = temp;
            }
        }
    }
}
int Sortlist(sequenlist* L, int choice) {
    int last = L->last;
    if (last == -1 || last == 0) {
        return 0;
    }
    if (choice == 0) {
        sortById(L);
    }
    else if (choice == 1) {
        sortByName(L);
    }
    else if (choice == 2) {
        sortByScore(L);
    }
    else {
        return 1;
    }
    return 2;
}
int Printlist(sequenlist* L) {
    if (L->last == -1) {
        return 0;
    }
    for (int i = 0; i <= L->last; i++) {
        printf("学号: %d, 姓名: %s,成绩: %d\n", L->data[i].id, L->data[i].name, L->data[i].score);
    }
    return 1;
}
int main(void) {
    int choice_1,choice_2;
    sequenlist* L;
    int res;
    L = (sequenlist*)malloc(sizeof(sequenlist));
    L->last = -1;
    int id;
    char name[10];
    int score;
    int listflag = 0;
    student dat;
    int index;
    while (1) {
        printf("请选择你要进行的操作:\n[1] 建表 [2] 插入 [3] 删除 [4] 查询 [5] 逆置 [6] 排序 [7] 打印顺序表 [8] 退出\n");
        scanf("%d", &choice_1);
        int fexit = 0;
        if (!(choice_1 == 1 || choice_1 == 8) && listflag == 0) {
            printf("请先建表！\n");
            continue;
        }
        switch (choice_1)
        {
        case 1:
            listflag = 1;
            printf("成功建表！\n");
            break;
        case 2:
            printf("请依次输入你要插入的学生信息（学号，姓名，成绩中间用空格分开)\n");
            scanf("%d %s %d", &id, name, &score);
            dat.id = id;
            strcpy(dat.name, name);
            dat.score = score;
            printf("请输入你要插入的序号（例如序号为零，则插入到最开头）\n");
            scanf("%d", &index);
            res = Insertlist(L, dat, index);
            if (res == 0) {
                printf("表格已满！\n");
            }
            else if (res == 1) {
                printf("序号非法!\n");
            }
            else {
                printf("插入成功!\n");
            }
            break;
        case 3:
            printf("请输入你要删除的序号（0代表第一位）\n");
            scanf("%d", &index);
            res = Deletelist(L, index);
            if (res == 0) {
                printf("序号非法!\n");
            }
            else {
                printf("删除成功!\n");
            }
            break;
        case 4:
            printf("请输入你要查询的序号（0代表第一位）\n");
            student* temp = (student*)malloc(sizeof(student));
            scanf("%d", &index);
            res = Getlist(L, index, temp);
            if (res == 0) {
                printf("序号非法!\n");
            }
            else {
                printf("查询成功!\n");
                printf("学号: %d, 姓名: %s,成绩: %d\n", temp->id, temp->name, temp->score);
            }
            break;
        case 5:
            res = Reverselist(L);
            if (res == 0) {
                printf("无法/无需逆置顺序表\n");
            }
            else {
                printf("逆置成功\n");
            }
            break;
        case 6:
            printf("请选择排序的关键字(0代表学号，1代表名字，2代表成绩）\n");
            scanf("%d", &choice_2);
            res = Sortlist(L, choice_2);
            if (res == 0) {
                printf("表格无需排序\n");
            }
            else if (res == 1) {
                printf("关键字非法!\n");
            }
            else {
                printf("排序成功");
            }
            break;
        case 7:
            res = Printlist(L);
            if (res == 0) {
                printf("无数据可打印！\n");
            }
            break;
        case 8:
            fexit = 1;
            break;
        default:
            printf("错误选项！\n");
            fexit = 1;
            break;
        }
        if (fexit == 1) {
            break;
        }
    }
    
    return 0;
}