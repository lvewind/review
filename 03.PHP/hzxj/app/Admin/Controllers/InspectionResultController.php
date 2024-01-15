<?php

namespace App\Admin\Controllers;

use App\Admin\Repositories\InspectionResult;
use App\Admin\Repositories\ProjectResult;
use App\Models\Department;
use Dcat\Admin\Form;
use Dcat\Admin\Grid;
use Dcat\Admin\Show;
use Dcat\Admin\Http\Controllers\AdminController;

class InspectionResultController extends AdminController
{
    /**
     * Make a grid builder.
     *
     * @return Grid
     */
    protected function grid()
    {
        return Grid::make(new InspectionResult(['department', 'scheduling']), function (Grid $grid) {
            $grid->selector(function (Grid\Tools\Selector $selector) {
                $all_departments = Department::all();
                $department = [];
                foreach  ($all_departments as $all_department){
                    $department[$all_department->id] = $all_department->name;
                }
//                var_dump($department);
                $selector->select('department_id', '部门', $department);
            });
            $grid->column('id')->sortable();
            $grid->column('name')->link(function ($value) {
                return admin_url('inspection-result/'.$this->id);
            });
            $grid->column('状态')->display(function (){
                return $this->inspection_status == 1 ? '正常'  : '<span style="color: red">异常</span>';
            });
            $grid->column('department.name', '部门');
            $grid->column('scheduling.name', '班次');
            $grid->column('inspector');
            $grid->column('管理确认')->display(function (){
                return $this->checked == 1 ? '<span style="color: gray">已确认</span>'  : '<span style="color: black">未确认</span>';
            });;
            $grid->column('created_at');
            $grid->column('updated_at')->sortable();

            $grid->filter(function (Grid\Filter $filter) {
                $filter->like('department.name', '部门');
                $filter->like('created_at', '时间');

            });
            $grid->disableBatchDelete();
            $grid->disableDeleteButton();
            $grid->disableEditButton();
            $grid->disableCreateButton();
            $grid->disableRowSelector();
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
        return Show::make($id, new InspectionResult(['department', 'scheduling']), function (Show $show) {
            $show->field('id');
            $show->field('name');
            $show->field('department.name', '部门');
//            $show->field('place_id');
            $show->field('scheduling.name', '班次');
            $show->field('inspector');
            $show->field('created_at');
            $show->field('updated_at');

            $show->relation('projects_result', '巡检项目结果', function ($model){

                $grid = new Grid( new ProjectResult);
                $grid->model()->where('inspection_result_id', $model->id);

                $grid->setResource('projects_result');
                $grid->id();
                $grid->name();

                $grid->column('项目结果')->display(function (){
                    return $this->project_status == 1 ? '正常'  : '<span style="color: red">异常</span>';
                });
                $grid->column('photo_url', '照片')->display(function ($photo_url) {
                    return $photo_url;
                })->image('http://hzxj.test', 100, 100);

                $grid->column('video_url', '录像')->display(function ($video_url){
                    if ($video_url){
                        return '<video height="100" controls><source src="'.$video_url.'" type="video/mp4">您的浏览器不支持Video标签。</video>';
                    }else{
                        return '';
                    }

                });
                $grid->column('note', '备注');

                $grid->disableCreateButton();
                $grid->disableColumnSelector();
                $grid->disableRowSelector();
                $grid->disableActions();
                return $grid;

            });

            $show->disableDeleteButton();
            $show->disableEditButton();
        });
    }

    /**
     * Make a form builder.
     *
     * @return Form
     */
    protected function form()
    {
        return Form::make(new InspectionResult(), function (Form $form) {
            $form->display('id');
            $form->text('name');
            $form->text('department_id');
            $form->text('place_id');
            $form->text('scheduling_id');
            $form->text('inspector');

            $form->display('created_at');
            $form->display('updated_at');
        });
    }
}
