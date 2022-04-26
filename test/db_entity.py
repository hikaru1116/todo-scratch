
import sys
# importモジュールのディレクトリを設定
sys.path.append('../')


if __name__ == "__main__":
    from todo_scratch.bk_app.entities.user_entity import UserEntity

    entity_info = UserEntity.class_info()
    print(entity_info)
