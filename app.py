from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

# 配置文件保存路径
DATA_DIR = 'data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)


# 首页路由
@app.route('/')
def index():
    """渲染首页"""
    return render_template('index.html')


# 保存定制信息API
@app.route('/api/save-customization', methods=['POST'])
def save_customization():
    """保存用户的定制信息"""
    try:
        # 获取JSON数据
        data = request.get_json()

        # 添加时间戳
        data['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 保存到文件
        filename = f"customization_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = os.path.join(DATA_DIR, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        return jsonify({
            'success': True,
            'message': '定制信息保存成功',
            'data': data
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'保存失败: {str(e)}'
        }), 500


# 联系我们API
@app.route('/api/contact', methods=['POST'])
def contact():
    """处理联系表单提交"""
    try:
        # 获取JSON数据
        data = request.get_json()

        # 添加时间戳
        data['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 保存到文件
        filename = f"contact_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = os.path.join(DATA_DIR, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        return jsonify({
            'success': True,
            'message': '留言已收到，我们会尽快回复您'
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'提交失败: {str(e)}'
        }), 500


# 健康检查
@app.route('/health')
def health():
    """健康检查接口"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })


if __name__ == '__main__':
    # 创建templates目录（如果不存在）
    if not os.path.exists('templates'):
        os.makedirs('templates')

    # 运行服务器
    app.run(debug=True, host='0.0.0.0', port=5000)