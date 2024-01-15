<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\HasMany;
use Dcat\Admin\Traits\HasDateTimeFormatter;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;
use Illuminate\Database\Eloquent\SoftDeletes;
use Illuminate\Database\Eloquent\Model;

class Place extends Model
{
    use HasDateTimeFormatter;
    use SoftDeletes;

    public function scheduling(): BelongsToMany
    {
        $pivotTable = 'place_scheduling'; // 中间表

        $relatedModel = Scheduling::class; // 关联模型类名

        return $this->belongsToMany($relatedModel, $pivotTable, 'place_id', 'scheduling_id');
    }

    public function projects(): HasMany
    {
        return $this->hasMany(Project::class, 'place_id');
    }

    public function department(): BelongsTo
    {
        return $this->belongsTo(Department::class, 'department_id');
    }

}
