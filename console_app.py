import task_list


if __name__ == '__main__':
    print('pending tasks:')
    print()
    print(task_list.get_pending_tasks())
    print()
    print('all tasks:')
    print()
    print(task_list.get_all_tasks())
