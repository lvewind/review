<?php

namespace App\Admin\Controllers;

use App\Admin\Repositories\Place;
use App\Models\Department;
use App\Models\Project;
use App\Models\Scheduling;
use Dcat\Admin\Form;
use Dcat\Admin\Grid;
use Dcat\Admin\Show;
use Dcat\Admin\Http\Controllers\AdminController;

class PlaceController extends AdminController
{
    /**
     * Make a grid builder.
     *
     * @return Grid
     */

    protected function grid()
    {
        $builder = Place::with('department');
        return Grid::make($builder, function (Grid $grid) {
            $grid->column('id')->sortable();
            $grid->column('name');
            $grid->column('department.name','部门名称');
            $grid->column('qrcode')->qrcode(function () {
                return 'http://192.168.13.24:5173/form/'.$this->id;
//                return 'http://hzxjvue.eihotel.com/form/'.$this->id;
            }, 300, 300);;
            $grid->column('created_at');
            $grid->column('updated_at')->sortable();

            $grid->filter(function (Grid\Filter $filter) {
                $filter->equal('id');
            });
        });
    }

    /**
     * Make a show builder.
     *
     * @param mixed $id
     *
     * @return Show
     */
    protected function detail($id)
    {
        return Show::make($id, new Place(), function (Show $show) {
            $show->field('id');
            $show->field('name');
            $show->field('department_id');
            $show->field('department_id');
            $show->field('department_id');
            $show->field('qrcode');
//            $show->field('created_at');
//            $show->field('updated_at');
        });
    }

    /**
     * Make a form builder.
     *
     * @return Form
     */
    protected function form()
    {
        $builder = Place::with(['scheduling', 'projects']);
        return Form::make($builder, function (Form $form) {
            $form->display('id');
            $form->text('name', '巡检地点')->required();

            $form->select('department_id')
                ->options(Department::all()->pluck('name', 'id'))
                ->required();

            $form->multipleSelect('scheduling', '班次')
                ->options(Scheduling::all()->pluck('name', 'id'))
                ->customFormat(function ($v) {
                    if (! $v) {
                        return [];
                    }

                    // 从数据库中查出的二维数组中转化成ID
                    return array_column($v, 'id');
                })
                ->required();

            $form->hasMany('projects', "项目", function (Form\NestedForm $form) {
                $form->text('name')->required();
//                $form->checkbox('options', "选项")->options([1 => '照片', 2 => '录像'])->saving(function ($value) {
//                    // 转化成json字符串保存到数据库
//                    return json_encode($value);
//                });

                $form->checkbox('photo', "")->options([1 => '拍照'])->saving(function ($value) {
                    // 转化成json字符串保存到数据库
                    if ($value) {
                        return 1;
                    }else{
                        return 0;
                    }

                });

                $form->checkbox('video', "")->options([1 => '录像'])->saving(function ($value) {
                    // 转化成json字符串保存到数据库
                    if ($value) {
                        return 1;
                    }else{
                        return 0;
                    }
                });


            });

//            $form->text('department_id');
//            $form->text('qrcode');
//
//            $form->display('created_at');
//            $form->display('updated_at');
        });
    }
}
